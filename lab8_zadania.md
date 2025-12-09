query GetAllTopics {
  allTopics {
    id
    name
    created
    # Pobieranie danych z powiązanej kategorii (ForeignKey)
    category {
      id
      name
      description
    }
  }
}

query GetCategoryById {
  categoryById(id: 1) {
    id
    name
    description
  }
}

query GetAllPosts {
  allPosts {
    id
    title
    text
    slug
    createdAt
    updatedAt
    # Relacja do tematu
    topic {
      name
    }
  }
}

query GetPostByTitle {
  postByTitle(title: "cos") {
    id
    text
    createdAt
  }
}

mutation CreateNewPost {
  createPost(title: "Mój nowy post", text: "Treść tego posta") {
    post {
      id
      title
      texts
      createdAt
    }
  }
}

mutation UpdateExistingPost {
  updatePost(title: "Tytuł do znalezienia", test: "Nowa treść posta") {
    post {
      id
      title
      text
      updatedAt
    }
  }
}