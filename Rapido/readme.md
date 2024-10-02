

### Protobuf POST Request Structure of Rapido

- **UserID**: `string` (2 constant bytes prefixed, 1 constant byte suffixed)
- **Latitude**: Encoded as `int64` (Fixed 64-bit, `uint64`/`double`, 8 bytes)
- **Longitude**: Encoded as `int64` (Fixed 64-bit, `uint64`/`double`, 8 bytes)  
  (1 constant byte between Latitude and Longitude)
- **appId**: `string`
- **AppVersion**: `string`  
  (1 constant byte between appId and AppVersion)

