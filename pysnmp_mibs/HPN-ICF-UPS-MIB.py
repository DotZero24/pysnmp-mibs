_E='hpnicfUpsIndex'
_D='HPN-ICF-UPS-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols('ENTITY-MIB','entPhysicalIndex')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpnicfUps=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,82))
class HpnicfActionType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('action',1),('invalid',2)))
_HpnicfUpsMibObjects_ObjectIdentity=ObjectIdentity
hpnicfUpsMibObjects=_HpnicfUpsMibObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,82,1))
_HpnicfUpsConfigEnable_Type=HpnicfActionType
_HpnicfUpsConfigEnable_Object=MibScalar
hpnicfUpsConfigEnable=_HpnicfUpsConfigEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,82,1,1),_HpnicfUpsConfigEnable_Type())
hpnicfUpsConfigEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfUpsConfigEnable.setStatus(_A)
_HpnicfUpsConfigTable_Object=MibTable
hpnicfUpsConfigTable=_HpnicfUpsConfigTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,82,1,2))
if mibBuilder.loadTexts:hpnicfUpsConfigTable.setStatus(_A)
_HpnicfUpsConfigEntry_Object=MibTableRow
hpnicfUpsConfigEntry=_HpnicfUpsConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,82,1,2,1))
hpnicfUpsConfigEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:hpnicfUpsConfigEntry.setStatus(_A)
_HpnicfUpsIndex_Type=Integer32
_HpnicfUpsIndex_Object=MibTableColumn
hpnicfUpsIndex=_HpnicfUpsIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,82,1,2,1,1),_HpnicfUpsIndex_Type())
hpnicfUpsIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:hpnicfUpsIndex.setStatus(_A)
class _HpnicfUpsType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('emersonUart',1),('mge',2),('common',3),('emersonEth',4),('liebert',5)))
_HpnicfUpsType_Type.__name__=_C
_HpnicfUpsType_Object=MibTableColumn
hpnicfUpsType=_HpnicfUpsType_Object((1,3,6,1,4,1,11,2,14,11,15,2,82,1,2,1,2),_HpnicfUpsType_Type())
hpnicfUpsType.setMaxAccess('read-only')
if mibBuilder.loadTexts:hpnicfUpsType.setStatus(_A)
_HpnicfUpsIpAddress_Type=InetAddress
_HpnicfUpsIpAddress_Object=MibTableColumn
hpnicfUpsIpAddress=_HpnicfUpsIpAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,82,1,2,1,3),_HpnicfUpsIpAddress_Type())
hpnicfUpsIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfUpsIpAddress.setStatus(_A)
_HpnicfUpsIpAddressType_Type=InetAddressType
_HpnicfUpsIpAddressType_Object=MibTableColumn
hpnicfUpsIpAddressType=_HpnicfUpsIpAddressType_Object((1,3,6,1,4,1,11,2,14,11,15,2,82,1,2,1,4),_HpnicfUpsIpAddressType_Type())
hpnicfUpsIpAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfUpsIpAddressType.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'HpnicfActionType':HpnicfActionType,'hpnicfUps':hpnicfUps,'hpnicfUpsMibObjects':hpnicfUpsMibObjects,'hpnicfUpsConfigEnable':hpnicfUpsConfigEnable,'hpnicfUpsConfigTable':hpnicfUpsConfigTable,'hpnicfUpsConfigEntry':hpnicfUpsConfigEntry,_E:hpnicfUpsIndex,'hpnicfUpsType':hpnicfUpsType,'hpnicfUpsIpAddress':hpnicfUpsIpAddress,'hpnicfUpsIpAddressType':hpnicfUpsIpAddressType})