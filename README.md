# Проект: CRUD для API Yatube

## Задача

В проекте api_yatube есть приложение posts с описанием моделей **Yatube**. Вам нужно реализовать API для всех моделей приложения.

API должен быть доступен только аутентифицированным пользователям. Используйте в проекте аутентификацию по токену **TokenAuthentication**.

Аутентифицированный пользователь авторизован на изменение и удаление своего контента, в остальных случаях доступ предоставляется только для чтения. При попытке изменить чужие данные должен возвращаться код ответа **403 Forbidden**.

Для взаимодействия с ресурсами опишите и настройте такие эндпоинты:
<ol>
  <li>
    api/v1/api-token-auth/ (POST): передаём логин и пароль, получаем токен.
  </li>
  <li>
    api/v1/posts/ (GET, POST): получаем список всех постов или создаём новый пост.
  </li>
  <li>
    api/v1/posts/{post_id}/ (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем пост с идентификатором{post_id}.
  </li>
  <li>
    api/v1/groups/ (GET): получаем список всех групп.
  </li>
  <li>
    api/v1/groups/{group_id}/ (GET): получаем информацию о группе с идентификатором {group_id}.
  </li>
  <li>
    идентификатором post_id  (POST): создаём новый комментарий для поста с идентификатором {post_id}.
  </li>
  <li> 
    api/v1/posts/{post_id}/comments/{comment_id}/ (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем комментарий с идентификатором {comment_id} в посте с  id=post_id.
  </li>
</ol>

В ответ на запросы POST, PUT и PATCH ваш API должен возвращать объект, который был добавлен или изменён.

Обязательное условие: работайте с моделью **Post** через **ModelViewSet**. 
