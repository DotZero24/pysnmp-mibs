_H='mitelGrpCmnInterfaces'
_G='mitelIfTblType'
_F='mitelIfNumber'
_E='read-only'
_D='ifIndex'
_C='IF-MIB'
_B='MITEL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_C,_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
mitel=ModuleIdentity((1,3,6,1,4,1,1027))
if mibBuilder.loadTexts:mitel.setRevisions(('2014-02-11 12:00','2011-07-14 00:00','2006-01-01 00:00','2005-04-12 21:34','2004-02-23 00:00','1999-02-23 00:00','1996-04-26 00:00'))
class MitelIfType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('dnic',1))
class MitelNotifyTransportType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('mitelNotifTransV1Trap',1),('mitelNotifTransV2Trap',2),('mitelNotifTransInform',3)))
_MitelIdentification_ObjectIdentity=ObjectIdentity
mitelIdentification=_MitelIdentification_ObjectIdentity((1,3,6,1,4,1,1027,1))
if mibBuilder.loadTexts:mitelIdentification.setStatus(_A)
_MitelIdMgmtPlatforms_ObjectIdentity=ObjectIdentity
mitelIdMgmtPlatforms=_MitelIdMgmtPlatforms_ObjectIdentity((1,3,6,1,4,1,1027,1,1))
if mibBuilder.loadTexts:mitelIdMgmtPlatforms.setStatus(_A)
_MitelIdCallServers_ObjectIdentity=ObjectIdentity
mitelIdCallServers=_MitelIdCallServers_ObjectIdentity((1,3,6,1,4,1,1027,1,2))
if mibBuilder.loadTexts:mitelIdCallServers.setStatus(_A)
_MitelIdCsMc2_ObjectIdentity=ObjectIdentity
mitelIdCsMc2=_MitelIdCsMc2_ObjectIdentity((1,3,6,1,4,1,1027,1,2,1))
if mibBuilder.loadTexts:mitelIdCsMc2.setStatus(_A)
_MitelIdCs2000Light_ObjectIdentity=ObjectIdentity
mitelIdCs2000Light=_MitelIdCs2000Light_ObjectIdentity((1,3,6,1,4,1,1027,1,2,2))
if mibBuilder.loadTexts:mitelIdCs2000Light.setStatus(_A)
_MitelIdCsIpera3000_ObjectIdentity=ObjectIdentity
mitelIdCsIpera3000=_MitelIdCsIpera3000_ObjectIdentity((1,3,6,1,4,1,1027,1,2,3))
if mibBuilder.loadTexts:mitelIdCsIpera3000.setStatus(_A)
_MitelIdTerminals_ObjectIdentity=ObjectIdentity
mitelIdTerminals=_MitelIdTerminals_ObjectIdentity((1,3,6,1,4,1,1027,1,3))
if mibBuilder.loadTexts:mitelIdTerminals.setStatus(_A)
_MitelIdInterfaces_ObjectIdentity=ObjectIdentity
mitelIdInterfaces=_MitelIdInterfaces_ObjectIdentity((1,3,6,1,4,1,1027,1,4))
if mibBuilder.loadTexts:mitelIdInterfaces.setStatus(_A)
_MitelIdCtiPlatforms_ObjectIdentity=ObjectIdentity
mitelIdCtiPlatforms=_MitelIdCtiPlatforms_ObjectIdentity((1,3,6,1,4,1,1027,1,5))
if mibBuilder.loadTexts:mitelIdCtiPlatforms.setStatus(_A)
_MitelIdApplicationPlatforms_ObjectIdentity=ObjectIdentity
mitelIdApplicationPlatforms=_MitelIdApplicationPlatforms_ObjectIdentity((1,3,6,1,4,1,1027,1,6))
if mibBuilder.loadTexts:mitelIdApplicationPlatforms.setStatus(_A)
_MitelExperimental_ObjectIdentity=ObjectIdentity
mitelExperimental=_MitelExperimental_ObjectIdentity((1,3,6,1,4,1,1027,2))
if mibBuilder.loadTexts:mitelExperimental.setStatus(_A)
_MitelExtensions_ObjectIdentity=ObjectIdentity
mitelExtensions=_MitelExtensions_ObjectIdentity((1,3,6,1,4,1,1027,3))
if mibBuilder.loadTexts:mitelExtensions.setStatus(_A)
_MitelExtInterfaces_ObjectIdentity=ObjectIdentity
mitelExtInterfaces=_MitelExtInterfaces_ObjectIdentity((1,3,6,1,4,1,1027,3,2))
if mibBuilder.loadTexts:mitelExtInterfaces.setStatus(_A)
_MitelIfNumber_Type=Integer32
_MitelIfNumber_Object=MibScalar
mitelIfNumber=_MitelIfNumber_Object((1,3,6,1,4,1,1027,3,2,1),_MitelIfNumber_Type())
mitelIfNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:mitelIfNumber.setStatus(_A)
_MitelIfTable_Object=MibTable
mitelIfTable=_MitelIfTable_Object((1,3,6,1,4,1,1027,3,2,2))
if mibBuilder.loadTexts:mitelIfTable.setStatus(_A)
_MitelIfTableEntry_Object=MibTableRow
mitelIfTableEntry=_MitelIfTableEntry_Object((1,3,6,1,4,1,1027,3,2,2,1))
mitelIfTableEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:mitelIfTableEntry.setStatus(_A)
_MitelIfTblType_Type=MitelIfType
_MitelIfTblType_Object=MibTableColumn
mitelIfTblType=_MitelIfTblType_Object((1,3,6,1,4,1,1027,3,2,2,1,1),_MitelIfTblType_Type())
mitelIfTblType.setMaxAccess(_E)
if mibBuilder.loadTexts:mitelIfTblType.setStatus(_A)
_MitelProprietary_ObjectIdentity=ObjectIdentity
mitelProprietary=_MitelProprietary_ObjectIdentity((1,3,6,1,4,1,1027,4))
if mibBuilder.loadTexts:mitelProprietary.setStatus(_A)
_MitelPropApplications_ObjectIdentity=ObjectIdentity
mitelPropApplications=_MitelPropApplications_ObjectIdentity((1,3,6,1,4,1,1027,4,1))
if mibBuilder.loadTexts:mitelPropApplications.setStatus(_A)
_MitelAppCallServer_ObjectIdentity=ObjectIdentity
mitelAppCallServer=_MitelAppCallServer_ObjectIdentity((1,3,6,1,4,1,1027,4,1,1))
if mibBuilder.loadTexts:mitelAppCallServer.setStatus(_A)
_MitelPropTransmission_ObjectIdentity=ObjectIdentity
mitelPropTransmission=_MitelPropTransmission_ObjectIdentity((1,3,6,1,4,1,1027,4,2))
if mibBuilder.loadTexts:mitelPropTransmission.setStatus(_A)
_MitelPropProtocols_ObjectIdentity=ObjectIdentity
mitelPropProtocols=_MitelPropProtocols_ObjectIdentity((1,3,6,1,4,1,1027,4,3))
if mibBuilder.loadTexts:mitelPropProtocols.setStatus(_A)
_MitelPropUtilities_ObjectIdentity=ObjectIdentity
mitelPropUtilities=_MitelPropUtilities_ObjectIdentity((1,3,6,1,4,1,1027,4,4))
if mibBuilder.loadTexts:mitelPropUtilities.setStatus(_A)
_MitelPropHardware_ObjectIdentity=ObjectIdentity
mitelPropHardware=_MitelPropHardware_ObjectIdentity((1,3,6,1,4,1,1027,4,5))
if mibBuilder.loadTexts:mitelPropHardware.setStatus(_A)
_MitelPropNotifications_ObjectIdentity=ObjectIdentity
mitelPropNotifications=_MitelPropNotifications_ObjectIdentity((1,3,6,1,4,1,1027,4,6))
if mibBuilder.loadTexts:mitelPropNotifications.setStatus(_A)
_MitelPropReset_ObjectIdentity=ObjectIdentity
mitelPropReset=_MitelPropReset_ObjectIdentity((1,3,6,1,4,1,1027,4,7))
if mibBuilder.loadTexts:mitelPropReset.setStatus(_A)
_MitelPropCommon_ObjectIdentity=ObjectIdentity
mitelPropCommon=_MitelPropCommon_ObjectIdentity((1,3,6,1,4,1,1027,4,9))
if mibBuilder.loadTexts:mitelPropCommon.setStatus(_A)
_MitelConformance_ObjectIdentity=ObjectIdentity
mitelConformance=_MitelConformance_ObjectIdentity((1,3,6,1,4,1,1027,5))
if mibBuilder.loadTexts:mitelConformance.setStatus(_A)
_MitelConfCompliances_ObjectIdentity=ObjectIdentity
mitelConfCompliances=_MitelConfCompliances_ObjectIdentity((1,3,6,1,4,1,1027,5,1))
if mibBuilder.loadTexts:mitelConfCompliances.setStatus(_A)
_MitelConfGroups_ObjectIdentity=ObjectIdentity
mitelConfGroups=_MitelConfGroups_ObjectIdentity((1,3,6,1,4,1,1027,5,2))
if mibBuilder.loadTexts:mitelConfGroups.setStatus(_A)
_MitelGrpCommon_ObjectIdentity=ObjectIdentity
mitelGrpCommon=_MitelGrpCommon_ObjectIdentity((1,3,6,1,4,1,1027,5,2,1))
if mibBuilder.loadTexts:mitelGrpCommon.setStatus(_A)
_MitelGrpCs2000_ObjectIdentity=ObjectIdentity
mitelGrpCs2000=_MitelGrpCs2000_ObjectIdentity((1,3,6,1,4,1,1027,5,2,3))
if mibBuilder.loadTexts:mitelGrpCs2000.setStatus(_A)
_MitelGrpIpera3000_ObjectIdentity=ObjectIdentity
mitelGrpIpera3000=_MitelGrpIpera3000_ObjectIdentity((1,3,6,1,4,1,1027,5,2,4))
if mibBuilder.loadTexts:mitelGrpIpera3000.setStatus(_A)
_MitelConfAgents_ObjectIdentity=ObjectIdentity
mitelConfAgents=_MitelConfAgents_ObjectIdentity((1,3,6,1,4,1,1027,5,3))
if mibBuilder.loadTexts:mitelConfAgents.setStatus(_A)
mitelGrpCmnInterfaces=ObjectGroup((1,3,6,1,4,1,1027,5,2,1,6))
mitelGrpCmnInterfaces.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:mitelGrpCmnInterfaces.setStatus(_A)
mitelComplMitel=ModuleCompliance((1,3,6,1,4,1,1027,5,1,1))
mitelComplMitel.setObjects((_B,_H))
if mibBuilder.loadTexts:mitelComplMitel.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'MitelIfType':MitelIfType,'MitelNotifyTransportType':MitelNotifyTransportType,'mitel':mitel,'mitelIdentification':mitelIdentification,'mitelIdMgmtPlatforms':mitelIdMgmtPlatforms,'mitelIdCallServers':mitelIdCallServers,'mitelIdCsMc2':mitelIdCsMc2,'mitelIdCs2000Light':mitelIdCs2000Light,'mitelIdCsIpera3000':mitelIdCsIpera3000,'mitelIdTerminals':mitelIdTerminals,'mitelIdInterfaces':mitelIdInterfaces,'mitelIdCtiPlatforms':mitelIdCtiPlatforms,'mitelIdApplicationPlatforms':mitelIdApplicationPlatforms,'mitelExperimental':mitelExperimental,'mitelExtensions':mitelExtensions,'mitelExtInterfaces':mitelExtInterfaces,_F:mitelIfNumber,'mitelIfTable':mitelIfTable,'mitelIfTableEntry':mitelIfTableEntry,_G:mitelIfTblType,'mitelProprietary':mitelProprietary,'mitelPropApplications':mitelPropApplications,'mitelAppCallServer':mitelAppCallServer,'mitelPropTransmission':mitelPropTransmission,'mitelPropProtocols':mitelPropProtocols,'mitelPropUtilities':mitelPropUtilities,'mitelPropHardware':mitelPropHardware,'mitelPropNotifications':mitelPropNotifications,'mitelPropReset':mitelPropReset,'mitelPropCommon':mitelPropCommon,'mitelConformance':mitelConformance,'mitelConfCompliances':mitelConfCompliances,'mitelComplMitel':mitelComplMitel,'mitelConfGroups':mitelConfGroups,'mitelGrpCommon':mitelGrpCommon,_H:mitelGrpCmnInterfaces,'mitelGrpCs2000':mitelGrpCs2000,'mitelGrpIpera3000':mitelGrpIpera3000,'mitelConfAgents':mitelConfAgents})