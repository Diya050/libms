<template>

  <div class="mx-20"><br><br>
    <div class="flex flex-row items-center justify-between">
      <h1 class="text-7xl font-algerian text-gray-1500">Library Books</h1>
      <Button icon-left="plus" @click="addArticleDialogShown = true">New Article</Button>
      
    </div>

    <div class="mt-2"><br><br>
      <Card title="Children Literature">
        <div><hr>
          <ul>
            <li
              class="flex flex-row space-y-2 items-center justify-between"
              v-for="article in articles.data"
              :key="article.name"
            >
              <router-link :to="`/articles/${article.name}`">
                {{ article.article_name }}
              </router-link>
              <Button @click="toggleBookStatus(article)" :icon="getBookStatusIcon(article)" />
            </li>
          </ul>

          
        </div>
      </Card>
    </div>

    <router-view></router-view>

    <Dialog
      :options="{
        title: 'Add New Article',
        actions: [
          {
            label: 'Add Article',
            appearance: 'primary',
            handler: ({ close }) => {
              addArticle()
              close() // closes dialog
            },
          },
          { label: 'Cancel' },
        ],
      }"
      v-model="addArticleDialogShown"
    >
      <template #body-content>
        <div class="space-y-2">
          <Input
            v-model="article.article_name"
            type="text"
            required
            placeholder="Enter the article name..."
            label="Article Name"
          />
          <Input
            v-model="article.image"
            type="text"
            placeholder="Add link"
            label="Image"
          />
          <Input
            v-model="article.author"
            type="text"
            required
            placeholder="Enter the author's name..."
            label="Author"
          />
          <Input
            v-model="article.description"
            type="textarea"
            placeholder="Enter the description..."
            label="Description"
          />
          <Input
            v-model="article.isbn"
            type="text"
            required
            placeholder="Enter the ISBN..."
            label="ISBN"
          />
          <Input
            v-model="article.status"
            type="select"
            :options="['Issued', 'Available']"
            label="Status"
          />
          <Input
            v-model="article.publisher"
            type="text"
            required
            placeholder="Enter the publisher..."
            label="Publisher"
          />
          <Input
            v-model="article.published"
            type="checkbox"
            label="Published"
          />
          <Input
            v-model="article.route"
            type="text"
            required
            placeholder="Enter the route..."
            label="Route"
          />
          <Input
            v-model="article.category"
            type="select"
            :options="categoryOptions"
            label="Category"
          />
        </div>
      </template>
    </Dialog>
  </div>
</template>

<script setup>
import { Dialog, createListResource, Card, Input, Button } from 'frappe-ui'
import { reactive, ref, computed } from 'vue'

const article = reactive({
  article_name: '',
  image: '',
  author: '',
  description: '',
  isbn: '',
  status: 'Available',
  publisher: '',
  published: false,
  route: '',
  category: '',
})

const addArticleDialogShown = ref(false)

const articles = createListResource({
  doctype: 'Article',
  fields: ['name', 'article_name', 'image', 'author', 'description', 'isbn', 'status', 'publisher', 'published', 'route', 'category'],
  limit: 100,
})
articles.reload()

const categories = createListResource({
  doctype: 'Category',
  fields: ['name'],
  limit: 100,
})
categories.reload()

const categoryOptions = computed(() => {
  if (categories.list.loading || !categories.data) {
    return []
  }
  return categories.data.map((category) => category.name)
})

const addArticle = () => {
  console.log(article)
  articles.insert.submit(article)
}

const toggleBookStatus = (article) => {
  if (article.status === 'Available') {
    article.status = 'Issued';
  } else {
    article.status = 'Available';
  }
  articles.update.submit(article);
}

const getBookStatusIcon = (article) => {
  return article.status === 'Available' ? 'check' : 'undo';
}


</script>

