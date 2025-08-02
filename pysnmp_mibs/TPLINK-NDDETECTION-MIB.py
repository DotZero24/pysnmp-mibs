_L='ndDetectionStatVlanId'
_K='ndDetectionVlanId'
_J='ifIndex'
_I='IF-MIB'
_H='TPLINK-NDDETECTION-MIB'
_G='OctetString'
_F='enable'
_E='disable'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_I,_J)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
tplinkNdDetectionMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,93))
if mibBuilder.loadTexts:tplinkNdDetectionMIB.setRevisions(('2012-12-17 10:14',))
_TplinkNdDetectionMIBObjects_ObjectIdentity=ObjectIdentity
tplinkNdDetectionMIBObjects=_TplinkNdDetectionMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,93,1))
_NdDetectionGlobalConfig_ObjectIdentity=ObjectIdentity
ndDetectionGlobalConfig=_NdDetectionGlobalConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,93,1,1))
class _NdDetectionEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_NdDetectionEnable_Type.__name__=_B
_NdDetectionEnable_Object=MibScalar
ndDetectionEnable=_NdDetectionEnable_Object((1,3,6,1,4,1,11863,6,93,1,1,1),_NdDetectionEnable_Type())
ndDetectionEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:ndDetectionEnable.setStatus(_A)
_NdDetectionVlanConfig_ObjectIdentity=ObjectIdentity
ndDetectionVlanConfig=_NdDetectionVlanConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,93,1,2))
_NdDetectionVlanConfigTable_Object=MibTable
ndDetectionVlanConfigTable=_NdDetectionVlanConfigTable_Object((1,3,6,1,4,1,11863,6,93,1,2,1))
if mibBuilder.loadTexts:ndDetectionVlanConfigTable.setStatus(_A)
_NdDetectionVlanConfigEntry_Object=MibTableRow
ndDetectionVlanConfigEntry=_NdDetectionVlanConfigEntry_Object((1,3,6,1,4,1,11863,6,93,1,2,1,1))
ndDetectionVlanConfigEntry.setIndexNames((0,_H,_K))
if mibBuilder.loadTexts:ndDetectionVlanConfigEntry.setStatus(_A)
class _NdDetectionVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_NdDetectionVlanId_Type.__name__=_B
_NdDetectionVlanId_Object=MibTableColumn
ndDetectionVlanId=_NdDetectionVlanId_Object((1,3,6,1,4,1,11863,6,93,1,2,1,1,1),_NdDetectionVlanId_Type())
ndDetectionVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:ndDetectionVlanId.setStatus(_A)
class _NdDetectionVlanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_NdDetectionVlanStatus_Type.__name__=_B
_NdDetectionVlanStatus_Object=MibTableColumn
ndDetectionVlanStatus=_NdDetectionVlanStatus_Object((1,3,6,1,4,1,11863,6,93,1,2,1,1,2),_NdDetectionVlanStatus_Type())
ndDetectionVlanStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ndDetectionVlanStatus.setStatus(_A)
class _NdDetectionVlanLogStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_NdDetectionVlanLogStatus_Type.__name__=_B
_NdDetectionVlanLogStatus_Object=MibTableColumn
ndDetectionVlanLogStatus=_NdDetectionVlanLogStatus_Object((1,3,6,1,4,1,11863,6,93,1,2,1,1,3),_NdDetectionVlanLogStatus_Type())
ndDetectionVlanLogStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ndDetectionVlanLogStatus.setStatus(_A)
_NdDetectionPortConfig_ObjectIdentity=ObjectIdentity
ndDetectionPortConfig=_NdDetectionPortConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,93,1,3))
_NdDetectionPortConfigTable_Object=MibTable
ndDetectionPortConfigTable=_NdDetectionPortConfigTable_Object((1,3,6,1,4,1,11863,6,93,1,3,1))
if mibBuilder.loadTexts:ndDetectionPortConfigTable.setStatus(_A)
_NdDetectionPortConfigEntry_Object=MibTableRow
ndDetectionPortConfigEntry=_NdDetectionPortConfigEntry_Object((1,3,6,1,4,1,11863,6,93,1,3,1,1))
ndDetectionPortConfigEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:ndDetectionPortConfigEntry.setStatus(_A)
class _NdDetectionPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NdDetectionPort_Type.__name__=_G
_NdDetectionPort_Object=MibTableColumn
ndDetectionPort=_NdDetectionPort_Object((1,3,6,1,4,1,11863,6,93,1,3,1,1,1),_NdDetectionPort_Type())
ndDetectionPort.setMaxAccess(_C)
if mibBuilder.loadTexts:ndDetectionPort.setStatus(_A)
class _NdDetectionPortConfigTrustedPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_NdDetectionPortConfigTrustedPort_Type.__name__=_B
_NdDetectionPortConfigTrustedPort_Object=MibTableColumn
ndDetectionPortConfigTrustedPort=_NdDetectionPortConfigTrustedPort_Object((1,3,6,1,4,1,11863,6,93,1,3,1,1,2),_NdDetectionPortConfigTrustedPort_Type())
ndDetectionPortConfigTrustedPort.setMaxAccess(_D)
if mibBuilder.loadTexts:ndDetectionPortConfigTrustedPort.setStatus(_A)
class _NdDetectionPortConfigPortLag_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_NdDetectionPortConfigPortLag_Type.__name__=_G
_NdDetectionPortConfigPortLag_Object=MibTableColumn
ndDetectionPortConfigPortLag=_NdDetectionPortConfigPortLag_Object((1,3,6,1,4,1,11863,6,93,1,3,1,1,3),_NdDetectionPortConfigPortLag_Type())
ndDetectionPortConfigPortLag.setMaxAccess(_C)
if mibBuilder.loadTexts:ndDetectionPortConfigPortLag.setStatus(_A)
_NdDetectionStatisticConfig_ObjectIdentity=ObjectIdentity
ndDetectionStatisticConfig=_NdDetectionStatisticConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,93,1,4))
class _NdDetectionStatReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('notReset',0),('reset',1)))
_NdDetectionStatReset_Type.__name__=_B
_NdDetectionStatReset_Object=MibScalar
ndDetectionStatReset=_NdDetectionStatReset_Object((1,3,6,1,4,1,11863,6,93,1,4,1),_NdDetectionStatReset_Type())
ndDetectionStatReset.setMaxAccess(_D)
if mibBuilder.loadTexts:ndDetectionStatReset.setStatus(_A)
_NdDetectionStatTable_Object=MibTable
ndDetectionStatTable=_NdDetectionStatTable_Object((1,3,6,1,4,1,11863,6,93,1,4,2))
if mibBuilder.loadTexts:ndDetectionStatTable.setStatus(_A)
_NdDetectionStatEntry_Object=MibTableRow
ndDetectionStatEntry=_NdDetectionStatEntry_Object((1,3,6,1,4,1,11863,6,93,1,4,2,1))
ndDetectionStatEntry.setIndexNames((0,_H,_L))
if mibBuilder.loadTexts:ndDetectionStatEntry.setStatus(_A)
class _NdDetectionStatVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_NdDetectionStatVlanId_Type.__name__=_B
_NdDetectionStatVlanId_Object=MibTableColumn
ndDetectionStatVlanId=_NdDetectionStatVlanId_Object((1,3,6,1,4,1,11863,6,93,1,4,2,1,1),_NdDetectionStatVlanId_Type())
ndDetectionStatVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:ndDetectionStatVlanId.setStatus(_A)
_NdDetectionStatForward_Type=Counter64
_NdDetectionStatForward_Object=MibTableColumn
ndDetectionStatForward=_NdDetectionStatForward_Object((1,3,6,1,4,1,11863,6,93,1,4,2,1,2),_NdDetectionStatForward_Type())
ndDetectionStatForward.setMaxAccess(_C)
if mibBuilder.loadTexts:ndDetectionStatForward.setStatus(_A)
_NdDetectionStatDrop_Type=Counter64
_NdDetectionStatDrop_Object=MibTableColumn
ndDetectionStatDrop=_NdDetectionStatDrop_Object((1,3,6,1,4,1,11863,6,93,1,4,2,1,3),_NdDetectionStatDrop_Type())
ndDetectionStatDrop.setMaxAccess(_C)
if mibBuilder.loadTexts:ndDetectionStatDrop.setStatus(_A)
_TplinkNdDetectionNotifications_ObjectIdentity=ObjectIdentity
tplinkNdDetectionNotifications=_TplinkNdDetectionNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,93,2))
mibBuilder.exportSymbols(_H,**{'tplinkNdDetectionMIB':tplinkNdDetectionMIB,'tplinkNdDetectionMIBObjects':tplinkNdDetectionMIBObjects,'ndDetectionGlobalConfig':ndDetectionGlobalConfig,'ndDetectionEnable':ndDetectionEnable,'ndDetectionVlanConfig':ndDetectionVlanConfig,'ndDetectionVlanConfigTable':ndDetectionVlanConfigTable,'ndDetectionVlanConfigEntry':ndDetectionVlanConfigEntry,_K:ndDetectionVlanId,'ndDetectionVlanStatus':ndDetectionVlanStatus,'ndDetectionVlanLogStatus':ndDetectionVlanLogStatus,'ndDetectionPortConfig':ndDetectionPortConfig,'ndDetectionPortConfigTable':ndDetectionPortConfigTable,'ndDetectionPortConfigEntry':ndDetectionPortConfigEntry,'ndDetectionPort':ndDetectionPort,'ndDetectionPortConfigTrustedPort':ndDetectionPortConfigTrustedPort,'ndDetectionPortConfigPortLag':ndDetectionPortConfigPortLag,'ndDetectionStatisticConfig':ndDetectionStatisticConfig,'ndDetectionStatReset':ndDetectionStatReset,'ndDetectionStatTable':ndDetectionStatTable,'ndDetectionStatEntry':ndDetectionStatEntry,_L:ndDetectionStatVlanId,'ndDetectionStatForward':ndDetectionStatForward,'ndDetectionStatDrop':ndDetectionStatDrop,'tplinkNdDetectionNotifications':tplinkNdDetectionNotifications})