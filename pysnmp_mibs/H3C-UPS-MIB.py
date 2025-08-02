_E='h3cUpsIndex'
_D='H3C-UPS-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols('ENTITY-MIB','entPhysicalIndex')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
h3cUps=ModuleIdentity((1,3,6,1,4,1,2011,10,2,82))
class H3cActionType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('action',1),('invalid',2)))
_H3cUpsMibObjects_ObjectIdentity=ObjectIdentity
h3cUpsMibObjects=_H3cUpsMibObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,82,1))
_H3cUpsConfigEnable_Type=H3cActionType
_H3cUpsConfigEnable_Object=MibScalar
h3cUpsConfigEnable=_H3cUpsConfigEnable_Object((1,3,6,1,4,1,2011,10,2,82,1,1),_H3cUpsConfigEnable_Type())
h3cUpsConfigEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cUpsConfigEnable.setStatus(_A)
_H3cUpsConfigTable_Object=MibTable
h3cUpsConfigTable=_H3cUpsConfigTable_Object((1,3,6,1,4,1,2011,10,2,82,1,2))
if mibBuilder.loadTexts:h3cUpsConfigTable.setStatus(_A)
_H3cUpsConfigEntry_Object=MibTableRow
h3cUpsConfigEntry=_H3cUpsConfigEntry_Object((1,3,6,1,4,1,2011,10,2,82,1,2,1))
h3cUpsConfigEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:h3cUpsConfigEntry.setStatus(_A)
_H3cUpsIndex_Type=Integer32
_H3cUpsIndex_Object=MibTableColumn
h3cUpsIndex=_H3cUpsIndex_Object((1,3,6,1,4,1,2011,10,2,82,1,2,1,1),_H3cUpsIndex_Type())
h3cUpsIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:h3cUpsIndex.setStatus(_A)
class _H3cUpsType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('emersonUart',1),('mge',2),('common',3),('emersonEth',4),('liebert',5)))
_H3cUpsType_Type.__name__=_C
_H3cUpsType_Object=MibTableColumn
h3cUpsType=_H3cUpsType_Object((1,3,6,1,4,1,2011,10,2,82,1,2,1,2),_H3cUpsType_Type())
h3cUpsType.setMaxAccess('read-only')
if mibBuilder.loadTexts:h3cUpsType.setStatus(_A)
_H3cUpsIpAddress_Type=InetAddress
_H3cUpsIpAddress_Object=MibTableColumn
h3cUpsIpAddress=_H3cUpsIpAddress_Object((1,3,6,1,4,1,2011,10,2,82,1,2,1,3),_H3cUpsIpAddress_Type())
h3cUpsIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cUpsIpAddress.setStatus(_A)
_H3cUpsIpAddressType_Type=InetAddressType
_H3cUpsIpAddressType_Object=MibTableColumn
h3cUpsIpAddressType=_H3cUpsIpAddressType_Object((1,3,6,1,4,1,2011,10,2,82,1,2,1,4),_H3cUpsIpAddressType_Type())
h3cUpsIpAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cUpsIpAddressType.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'H3cActionType':H3cActionType,'h3cUps':h3cUps,'h3cUpsMibObjects':h3cUpsMibObjects,'h3cUpsConfigEnable':h3cUpsConfigEnable,'h3cUpsConfigTable':h3cUpsConfigTable,'h3cUpsConfigEntry':h3cUpsConfigEntry,_E:h3cUpsIndex,'h3cUpsType':h3cUpsType,'h3cUpsIpAddress':h3cUpsIpAddress,'h3cUpsIpAddressType':h3cUpsIpAddressType})