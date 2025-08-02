_K='arpInspectionStatVlanId'
_J='arpInspectionVlanId'
_I='ifIndex'
_H='IF-MIB'
_G='TPLINK-ARP-INSPECTION-MIB'
_F='enable'
_E='disable'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_H,_I)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
tplinkArpInspectionMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,28))
if mibBuilder.loadTexts:tplinkArpInspectionMIB.setRevisions(('2012-12-13 09:30',))
_TplinkArpInspectionMIBObjects_ObjectIdentity=ObjectIdentity
tplinkArpInspectionMIBObjects=_TplinkArpInspectionMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,28,1))
_ArpInspectionGlobalConfig_ObjectIdentity=ObjectIdentity
arpInspectionGlobalConfig=_ArpInspectionGlobalConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,28,1,1))
class _ArpInspectionGlobalEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_ArpInspectionGlobalEnable_Type.__name__=_B
_ArpInspectionGlobalEnable_Object=MibScalar
arpInspectionGlobalEnable=_ArpInspectionGlobalEnable_Object((1,3,6,1,4,1,11863,6,28,1,1,1),_ArpInspectionGlobalEnable_Type())
arpInspectionGlobalEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:arpInspectionGlobalEnable.setStatus(_A)
class _ArpInspectionVerifySmac_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_ArpInspectionVerifySmac_Type.__name__=_B
_ArpInspectionVerifySmac_Object=MibScalar
arpInspectionVerifySmac=_ArpInspectionVerifySmac_Object((1,3,6,1,4,1,11863,6,28,1,1,2),_ArpInspectionVerifySmac_Type())
arpInspectionVerifySmac.setMaxAccess(_C)
if mibBuilder.loadTexts:arpInspectionVerifySmac.setStatus(_A)
class _ArpInspectionVerifyDmac_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_ArpInspectionVerifyDmac_Type.__name__=_B
_ArpInspectionVerifyDmac_Object=MibScalar
arpInspectionVerifyDmac=_ArpInspectionVerifyDmac_Object((1,3,6,1,4,1,11863,6,28,1,1,3),_ArpInspectionVerifyDmac_Type())
arpInspectionVerifyDmac.setMaxAccess(_C)
if mibBuilder.loadTexts:arpInspectionVerifyDmac.setStatus(_A)
class _ArpInspectionVerifyIp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_ArpInspectionVerifyIp_Type.__name__=_B
_ArpInspectionVerifyIp_Object=MibScalar
arpInspectionVerifyIp=_ArpInspectionVerifyIp_Object((1,3,6,1,4,1,11863,6,28,1,1,4),_ArpInspectionVerifyIp_Type())
arpInspectionVerifyIp.setMaxAccess(_C)
if mibBuilder.loadTexts:arpInspectionVerifyIp.setStatus(_A)
_ArpInspectionVlanConfig_ObjectIdentity=ObjectIdentity
arpInspectionVlanConfig=_ArpInspectionVlanConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,28,1,2))
_ArpInspectionVlanConfigTable_Object=MibTable
arpInspectionVlanConfigTable=_ArpInspectionVlanConfigTable_Object((1,3,6,1,4,1,11863,6,28,1,2,1))
if mibBuilder.loadTexts:arpInspectionVlanConfigTable.setStatus(_A)
_ArpInspectionVlanConfigEntry_Object=MibTableRow
arpInspectionVlanConfigEntry=_ArpInspectionVlanConfigEntry_Object((1,3,6,1,4,1,11863,6,28,1,2,1,1))
arpInspectionVlanConfigEntry.setIndexNames((0,_G,_J))
if mibBuilder.loadTexts:arpInspectionVlanConfigEntry.setStatus(_A)
class _ArpInspectionVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_ArpInspectionVlanId_Type.__name__=_B
_ArpInspectionVlanId_Object=MibTableColumn
arpInspectionVlanId=_ArpInspectionVlanId_Object((1,3,6,1,4,1,11863,6,28,1,2,1,1,1),_ArpInspectionVlanId_Type())
arpInspectionVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:arpInspectionVlanId.setStatus(_A)
class _ArpInspectionVlanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_ArpInspectionVlanStatus_Type.__name__=_B
_ArpInspectionVlanStatus_Object=MibTableColumn
arpInspectionVlanStatus=_ArpInspectionVlanStatus_Object((1,3,6,1,4,1,11863,6,28,1,2,1,1,2),_ArpInspectionVlanStatus_Type())
arpInspectionVlanStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:arpInspectionVlanStatus.setStatus(_A)
class _ArpInspectionVlanLogStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_ArpInspectionVlanLogStatus_Type.__name__=_B
_ArpInspectionVlanLogStatus_Object=MibTableColumn
arpInspectionVlanLogStatus=_ArpInspectionVlanLogStatus_Object((1,3,6,1,4,1,11863,6,28,1,2,1,1,3),_ArpInspectionVlanLogStatus_Type())
arpInspectionVlanLogStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:arpInspectionVlanLogStatus.setStatus(_A)
_ArpInspectionPortConfig_ObjectIdentity=ObjectIdentity
arpInspectionPortConfig=_ArpInspectionPortConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,28,1,3))
_ArpInspectionPortConfigTable_Object=MibTable
arpInspectionPortConfigTable=_ArpInspectionPortConfigTable_Object((1,3,6,1,4,1,11863,6,28,1,3,1))
if mibBuilder.loadTexts:arpInspectionPortConfigTable.setStatus(_A)
_ArpInspectionPortConfigEntry_Object=MibTableRow
arpInspectionPortConfigEntry=_ArpInspectionPortConfigEntry_Object((1,3,6,1,4,1,11863,6,28,1,3,1,1))
arpInspectionPortConfigEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:arpInspectionPortConfigEntry.setStatus(_A)
_ArpInspectionPortConfigPort_Type=OctetString
_ArpInspectionPortConfigPort_Object=MibTableColumn
arpInspectionPortConfigPort=_ArpInspectionPortConfigPort_Object((1,3,6,1,4,1,11863,6,28,1,3,1,1,1),_ArpInspectionPortConfigPort_Type())
arpInspectionPortConfigPort.setMaxAccess(_D)
if mibBuilder.loadTexts:arpInspectionPortConfigPort.setStatus(_A)
class _ArpInspectionPortConfigTrust_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_ArpInspectionPortConfigTrust_Type.__name__=_B
_ArpInspectionPortConfigTrust_Object=MibTableColumn
arpInspectionPortConfigTrust=_ArpInspectionPortConfigTrust_Object((1,3,6,1,4,1,11863,6,28,1,3,1,1,2),_ArpInspectionPortConfigTrust_Type())
arpInspectionPortConfigTrust.setMaxAccess(_C)
if mibBuilder.loadTexts:arpInspectionPortConfigTrust.setStatus(_A)
_ArpInspectionPortConfigLimitRate_Type=Integer32
_ArpInspectionPortConfigLimitRate_Object=MibTableColumn
arpInspectionPortConfigLimitRate=_ArpInspectionPortConfigLimitRate_Object((1,3,6,1,4,1,11863,6,28,1,3,1,1,3),_ArpInspectionPortConfigLimitRate_Type())
arpInspectionPortConfigLimitRate.setMaxAccess(_C)
if mibBuilder.loadTexts:arpInspectionPortConfigLimitRate.setStatus(_A)
_ArpInspectionPortConfigCurrentSpeed_Type=Integer32
_ArpInspectionPortConfigCurrentSpeed_Object=MibTableColumn
arpInspectionPortConfigCurrentSpeed=_ArpInspectionPortConfigCurrentSpeed_Object((1,3,6,1,4,1,11863,6,28,1,3,1,1,4),_ArpInspectionPortConfigCurrentSpeed_Type())
arpInspectionPortConfigCurrentSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:arpInspectionPortConfigCurrentSpeed.setStatus(_A)
_ArpInspectionPortConfigBurstInterval_Type=Integer32
_ArpInspectionPortConfigBurstInterval_Object=MibTableColumn
arpInspectionPortConfigBurstInterval=_ArpInspectionPortConfigBurstInterval_Object((1,3,6,1,4,1,11863,6,28,1,3,1,1,5),_ArpInspectionPortConfigBurstInterval_Type())
arpInspectionPortConfigBurstInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:arpInspectionPortConfigBurstInterval.setStatus(_A)
class _ArpInspectionPortConfigStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('normal',0),('down',1)))
_ArpInspectionPortConfigStatus_Type.__name__=_B
_ArpInspectionPortConfigStatus_Object=MibTableColumn
arpInspectionPortConfigStatus=_ArpInspectionPortConfigStatus_Object((1,3,6,1,4,1,11863,6,28,1,3,1,1,6),_ArpInspectionPortConfigStatus_Type())
arpInspectionPortConfigStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:arpInspectionPortConfigStatus.setStatus(_A)
class _ArpInspectionPortConfigRecover_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('none',0),('recover',1)))
_ArpInspectionPortConfigRecover_Type.__name__=_B
_ArpInspectionPortConfigRecover_Object=MibTableColumn
arpInspectionPortConfigRecover=_ArpInspectionPortConfigRecover_Object((1,3,6,1,4,1,11863,6,28,1,3,1,1,7),_ArpInspectionPortConfigRecover_Type())
arpInspectionPortConfigRecover.setMaxAccess(_C)
if mibBuilder.loadTexts:arpInspectionPortConfigRecover.setStatus(_A)
_ArpInspectionPortConfigPortLag_Type=OctetString
_ArpInspectionPortConfigPortLag_Object=MibTableColumn
arpInspectionPortConfigPortLag=_ArpInspectionPortConfigPortLag_Object((1,3,6,1,4,1,11863,6,28,1,3,1,1,8),_ArpInspectionPortConfigPortLag_Type())
arpInspectionPortConfigPortLag.setMaxAccess(_D)
if mibBuilder.loadTexts:arpInspectionPortConfigPortLag.setStatus(_A)
_ArpInspectionStatisticConfig_ObjectIdentity=ObjectIdentity
arpInspectionStatisticConfig=_ArpInspectionStatisticConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,28,1,4))
class _ArpInspectionStatReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('notReset',0),('reset',1)))
_ArpInspectionStatReset_Type.__name__=_B
_ArpInspectionStatReset_Object=MibScalar
arpInspectionStatReset=_ArpInspectionStatReset_Object((1,3,6,1,4,1,11863,6,28,1,4,1),_ArpInspectionStatReset_Type())
arpInspectionStatReset.setMaxAccess(_C)
if mibBuilder.loadTexts:arpInspectionStatReset.setStatus(_A)
_ArpInspectionStatTable_Object=MibTable
arpInspectionStatTable=_ArpInspectionStatTable_Object((1,3,6,1,4,1,11863,6,28,1,4,2))
if mibBuilder.loadTexts:arpInspectionStatTable.setStatus(_A)
_ArpInspectionStatEntry_Object=MibTableRow
arpInspectionStatEntry=_ArpInspectionStatEntry_Object((1,3,6,1,4,1,11863,6,28,1,4,2,1))
arpInspectionStatEntry.setIndexNames((0,_G,_K))
if mibBuilder.loadTexts:arpInspectionStatEntry.setStatus(_A)
class _ArpInspectionStatVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_ArpInspectionStatVlanId_Type.__name__=_B
_ArpInspectionStatVlanId_Object=MibTableColumn
arpInspectionStatVlanId=_ArpInspectionStatVlanId_Object((1,3,6,1,4,1,11863,6,28,1,4,2,1,1),_ArpInspectionStatVlanId_Type())
arpInspectionStatVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:arpInspectionStatVlanId.setStatus(_A)
_ArpInspectionStatForward_Type=Counter64
_ArpInspectionStatForward_Object=MibTableColumn
arpInspectionStatForward=_ArpInspectionStatForward_Object((1,3,6,1,4,1,11863,6,28,1,4,2,1,2),_ArpInspectionStatForward_Type())
arpInspectionStatForward.setMaxAccess(_D)
if mibBuilder.loadTexts:arpInspectionStatForward.setStatus(_A)
_ArpInspectionStatDrop_Type=Counter64
_ArpInspectionStatDrop_Object=MibTableColumn
arpInspectionStatDrop=_ArpInspectionStatDrop_Object((1,3,6,1,4,1,11863,6,28,1,4,2,1,3),_ArpInspectionStatDrop_Type())
arpInspectionStatDrop.setMaxAccess(_D)
if mibBuilder.loadTexts:arpInspectionStatDrop.setStatus(_A)
_TplinkArpInspectionNotifications_ObjectIdentity=ObjectIdentity
tplinkArpInspectionNotifications=_TplinkArpInspectionNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,28,2))
arpInspectionRxIllegalArpPacket=NotificationType((1,3,6,1,4,1,11863,6,28,2,1))
if mibBuilder.loadTexts:arpInspectionRxIllegalArpPacket.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'tplinkArpInspectionMIB':tplinkArpInspectionMIB,'tplinkArpInspectionMIBObjects':tplinkArpInspectionMIBObjects,'arpInspectionGlobalConfig':arpInspectionGlobalConfig,'arpInspectionGlobalEnable':arpInspectionGlobalEnable,'arpInspectionVerifySmac':arpInspectionVerifySmac,'arpInspectionVerifyDmac':arpInspectionVerifyDmac,'arpInspectionVerifyIp':arpInspectionVerifyIp,'arpInspectionVlanConfig':arpInspectionVlanConfig,'arpInspectionVlanConfigTable':arpInspectionVlanConfigTable,'arpInspectionVlanConfigEntry':arpInspectionVlanConfigEntry,_J:arpInspectionVlanId,'arpInspectionVlanStatus':arpInspectionVlanStatus,'arpInspectionVlanLogStatus':arpInspectionVlanLogStatus,'arpInspectionPortConfig':arpInspectionPortConfig,'arpInspectionPortConfigTable':arpInspectionPortConfigTable,'arpInspectionPortConfigEntry':arpInspectionPortConfigEntry,'arpInspectionPortConfigPort':arpInspectionPortConfigPort,'arpInspectionPortConfigTrust':arpInspectionPortConfigTrust,'arpInspectionPortConfigLimitRate':arpInspectionPortConfigLimitRate,'arpInspectionPortConfigCurrentSpeed':arpInspectionPortConfigCurrentSpeed,'arpInspectionPortConfigBurstInterval':arpInspectionPortConfigBurstInterval,'arpInspectionPortConfigStatus':arpInspectionPortConfigStatus,'arpInspectionPortConfigRecover':arpInspectionPortConfigRecover,'arpInspectionPortConfigPortLag':arpInspectionPortConfigPortLag,'arpInspectionStatisticConfig':arpInspectionStatisticConfig,'arpInspectionStatReset':arpInspectionStatReset,'arpInspectionStatTable':arpInspectionStatTable,'arpInspectionStatEntry':arpInspectionStatEntry,_K:arpInspectionStatVlanId,'arpInspectionStatForward':arpInspectionStatForward,'arpInspectionStatDrop':arpInspectionStatDrop,'tplinkArpInspectionNotifications':tplinkArpInspectionNotifications,'arpInspectionRxIllegalArpPacket':arpInspectionRxIllegalArpPacket})