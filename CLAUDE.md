# Claude Code Assistant Guidelines

## Build & Test Commands
- Build: `npm run build` or `yarn build`
- Lint: `npm run lint` or `yarn lint`
- Test all: `npm test` or `yarn test`
- Test single file: `npm test -- path/to/test.js` or `yarn test path/to/test.js`
- Type check: `npm run typecheck` or `yarn typecheck`

## Code Style Guidelines
- **Formatting**: Use Prettier with default configuration
- **Naming**: camelCase for variables/functions, PascalCase for classes/components
- **Imports**: Group and order by: built-in, external, internal, relative
- **Types**: Use TypeScript with explicit return types on exported functions
- **Error Handling**: Use try/catch blocks with specific error types when possible
- **Documentation**: JSDoc for public APIs, inline comments for complex logic only
- **Testing**: Write unit tests for all business logic, use descriptive test names

Customize these guidelines as your project evolves. Update this file when discovering new conventions or useful commands.