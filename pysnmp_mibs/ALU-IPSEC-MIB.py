_I='aluIPsecGroup'
_H='aluIPsecMdaDpStatsGroup'
_G='aluExtIPsecTunnelCopyDfBit'
_F='aluExtIPsecMdaDpStatsIPFragDrop'
_E='aluExtIPsecTunnelEntry'
_D='aluExtIPsecMdaDpStatsEntry'
_C='TruthValue'
_B='ALU-IPSEC-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
aluSARConfs,aluSARMIBModules,aluSARNotifyPrefix,aluSARObjs=mibBuilder.importSymbols('ALU-SAR-GLOBAL-MIB','aluSARConfs','aluSARMIBModules','aluSARNotifyPrefix','aluSARObjs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_C)
tmnxCardSlotNum,tmnxChassisIndex,tmnxMDASlotNum=mibBuilder.importSymbols('TIMETRA-CHASSIS-MIB','tmnxCardSlotNum','tmnxChassisIndex','tmnxMDASlotNum')
tmnxIPsecMdaDpStatsEntry,tmnxIPsecTunnelEntry=mibBuilder.importSymbols('TIMETRA-IPSEC-MIB','tmnxIPsecMdaDpStatsEntry','tmnxIPsecTunnelEntry')
sapEncapValue,sapPortId=mibBuilder.importSymbols('TIMETRA-SAP-MIB','sapEncapValue','sapPortId')
svcId,=mibBuilder.importSymbols('TIMETRA-SERV-MIB','svcId')
aluIPsecMIBModule=ModuleIdentity((1,3,6,1,4,1,6527,6,1,1,1,3,16))
if mibBuilder.loadTexts:aluIPsecMIBModule.setRevisions(('2011-04-18 00:00',))
_AluIPsecMIBConformance_ObjectIdentity=ObjectIdentity
aluIPsecMIBConformance=_AluIPsecMIBConformance_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,1,19))
_AluIPsecMIBCompliances_ObjectIdentity=ObjectIdentity
aluIPsecMIBCompliances=_AluIPsecMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,1,19,1))
_AluIPsecMIBGroups_ObjectIdentity=ObjectIdentity
aluIPsecMIBGroups=_AluIPsecMIBGroups_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,1,19,2))
_AluIPsecObjects_ObjectIdentity=ObjectIdentity
aluIPsecObjects=_AluIPsecObjects_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,2,19))
_AluExtIPsecMdaDpStatsTable_Object=MibTable
aluExtIPsecMdaDpStatsTable=_AluExtIPsecMdaDpStatsTable_Object((1,3,6,1,4,1,6527,6,1,2,2,19,1))
if mibBuilder.loadTexts:aluExtIPsecMdaDpStatsTable.setStatus(_A)
_AluExtIPsecMdaDpStatsEntry_Object=MibTableRow
aluExtIPsecMdaDpStatsEntry=_AluExtIPsecMdaDpStatsEntry_Object((1,3,6,1,4,1,6527,6,1,2,2,19,1,1))
if mibBuilder.loadTexts:aluExtIPsecMdaDpStatsEntry.setStatus(_A)
_AluExtIPsecMdaDpStatsIPFragDrop_Type=Counter64
_AluExtIPsecMdaDpStatsIPFragDrop_Object=MibTableColumn
aluExtIPsecMdaDpStatsIPFragDrop=_AluExtIPsecMdaDpStatsIPFragDrop_Object((1,3,6,1,4,1,6527,6,1,2,2,19,1,1,1),_AluExtIPsecMdaDpStatsIPFragDrop_Type())
aluExtIPsecMdaDpStatsIPFragDrop.setMaxAccess('read-only')
if mibBuilder.loadTexts:aluExtIPsecMdaDpStatsIPFragDrop.setStatus(_A)
_AluExtIPsecTunnelTable_Object=MibTable
aluExtIPsecTunnelTable=_AluExtIPsecTunnelTable_Object((1,3,6,1,4,1,6527,6,1,2,2,19,2))
if mibBuilder.loadTexts:aluExtIPsecTunnelTable.setStatus(_A)
_AluExtIPsecTunnelEntry_Object=MibTableRow
aluExtIPsecTunnelEntry=_AluExtIPsecTunnelEntry_Object((1,3,6,1,4,1,6527,6,1,2,2,19,2,1))
if mibBuilder.loadTexts:aluExtIPsecTunnelEntry.setStatus(_A)
class _AluExtIPsecTunnelCopyDfBit_Type(TruthValue):defaultValue=2
_AluExtIPsecTunnelCopyDfBit_Type.__name__=_C
_AluExtIPsecTunnelCopyDfBit_Object=MibTableColumn
aluExtIPsecTunnelCopyDfBit=_AluExtIPsecTunnelCopyDfBit_Object((1,3,6,1,4,1,6527,6,1,2,2,19,2,1,1),_AluExtIPsecTunnelCopyDfBit_Type())
aluExtIPsecTunnelCopyDfBit.setMaxAccess('read-create')
if mibBuilder.loadTexts:aluExtIPsecTunnelCopyDfBit.setStatus(_A)
_AluIPsecNotificationsPrefix_ObjectIdentity=ObjectIdentity
aluIPsecNotificationsPrefix=_AluIPsecNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,3,15))
_AluIPsecNotifications_ObjectIdentity=ObjectIdentity
aluIPsecNotifications=_AluIPsecNotifications_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,3,15,0))
tmnxIPsecMdaDpStatsEntry.registerAugmentions((_B,_D))
aluExtIPsecMdaDpStatsEntry.setIndexNames(*tmnxIPsecMdaDpStatsEntry.getIndexNames())
tmnxIPsecTunnelEntry.registerAugmentions((_B,_E))
aluExtIPsecTunnelEntry.setIndexNames(*tmnxIPsecTunnelEntry.getIndexNames())
aluIPsecMdaDpStatsGroup=ObjectGroup((1,3,6,1,4,1,6527,6,1,2,1,19,2,1))
aluIPsecMdaDpStatsGroup.setObjects((_B,_F))
if mibBuilder.loadTexts:aluIPsecMdaDpStatsGroup.setStatus(_A)
aluIPsecGroup=ObjectGroup((1,3,6,1,4,1,6527,6,1,2,1,19,2,2))
aluIPsecGroup.setObjects((_B,_G))
if mibBuilder.loadTexts:aluIPsecGroup.setStatus(_A)
aluIPsec7705V6v1Compliance=ModuleCompliance((1,3,6,1,4,1,6527,6,1,2,1,19,1,1))
aluIPsec7705V6v1Compliance.setObjects(*((_B,_H),(_B,_I)))
if mibBuilder.loadTexts:aluIPsec7705V6v1Compliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'aluIPsecMIBModule':aluIPsecMIBModule,'aluIPsecMIBConformance':aluIPsecMIBConformance,'aluIPsecMIBCompliances':aluIPsecMIBCompliances,'aluIPsec7705V6v1Compliance':aluIPsec7705V6v1Compliance,'aluIPsecMIBGroups':aluIPsecMIBGroups,_H:aluIPsecMdaDpStatsGroup,_I:aluIPsecGroup,'aluIPsecObjects':aluIPsecObjects,'aluExtIPsecMdaDpStatsTable':aluExtIPsecMdaDpStatsTable,_D:aluExtIPsecMdaDpStatsEntry,_F:aluExtIPsecMdaDpStatsIPFragDrop,'aluExtIPsecTunnelTable':aluExtIPsecTunnelTable,_E:aluExtIPsecTunnelEntry,_G:aluExtIPsecTunnelCopyDfBit,'aluIPsecNotificationsPrefix':aluIPsecNotificationsPrefix,'aluIPsecNotifications':aluIPsecNotifications})