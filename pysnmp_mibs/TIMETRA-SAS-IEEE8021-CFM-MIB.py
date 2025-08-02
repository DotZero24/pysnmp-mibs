_I='tmnxSASDot1agCfmMepGroupV2v0'
_H='tmnxDot1agCfmMepControlSapTag'
_G='tmnxDot1agCfmMepExtnEntry'
_F='read-create'
_E='TruthValue'
_D='Unsigned32'
_C='tmnxDot1agCfmMepSendAisOnPortDown'
_B='TIMETRA-SAS-IEEE8021-CFM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1agCfmMepEntry,=mibBuilder.importSymbols('IEEE8021-CFM-MIB','dot1agCfmMepEntry')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_E)
timetraSASConfs,timetraSASModules,timetraSASObjs=mibBuilder.importSymbols('TIMETRA-SAS-GLOBAL-MIB','timetraSASConfs','timetraSASModules','timetraSASObjs')
timetraSASIEEE8021CfmMIBModule=ModuleIdentity((1,3,6,1,4,1,6527,6,2,1,1,11))
if mibBuilder.loadTexts:timetraSASIEEE8021CfmMIBModule.setRevisions(('1910-01-01 00:00',))
_TmnxSASDot1agMIBConformance_ObjectIdentity=ObjectIdentity
tmnxSASDot1agMIBConformance=_TmnxSASDot1agMIBConformance_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,1,7))
_TmnxSASDot1agCfmCompliances_ObjectIdentity=ObjectIdentity
tmnxSASDot1agCfmCompliances=_TmnxSASDot1agCfmCompliances_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,1,7,1))
_TmnxSASDot1agCfmGroups_ObjectIdentity=ObjectIdentity
tmnxSASDot1agCfmGroups=_TmnxSASDot1agCfmGroups_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,1,7,2))
_TmnxSASDot1agMIBObjs_ObjectIdentity=ObjectIdentity
tmnxSASDot1agMIBObjs=_TmnxSASDot1agMIBObjs_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,2,11))
_TmnxSASDot1agCfmMep_ObjectIdentity=ObjectIdentity
tmnxSASDot1agCfmMep=_TmnxSASDot1agCfmMep_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,2,11,1))
_TmnxDot1agCfmMepExtnTable_Object=MibTable
tmnxDot1agCfmMepExtnTable=_TmnxDot1agCfmMepExtnTable_Object((1,3,6,1,4,1,6527,6,2,2,2,11,1,1))
if mibBuilder.loadTexts:tmnxDot1agCfmMepExtnTable.setStatus(_A)
_TmnxDot1agCfmMepExtnEntry_Object=MibTableRow
tmnxDot1agCfmMepExtnEntry=_TmnxDot1agCfmMepExtnEntry_Object((1,3,6,1,4,1,6527,6,2,2,2,11,1,1,1))
if mibBuilder.loadTexts:tmnxDot1agCfmMepExtnEntry.setStatus(_A)
class _TmnxDot1agCfmMepSendAisOnPortDown_Type(TruthValue):defaultValue=2
_TmnxDot1agCfmMepSendAisOnPortDown_Type.__name__=_E
_TmnxDot1agCfmMepSendAisOnPortDown_Object=MibTableColumn
tmnxDot1agCfmMepSendAisOnPortDown=_TmnxDot1agCfmMepSendAisOnPortDown_Object((1,3,6,1,4,1,6527,6,2,2,2,11,1,1,1,1),_TmnxDot1agCfmMepSendAisOnPortDown_Type())
tmnxDot1agCfmMepSendAisOnPortDown.setMaxAccess(_F)
if mibBuilder.loadTexts:tmnxDot1agCfmMepSendAisOnPortDown.setStatus(_A)
class _TmnxDot1agCfmMepControlSapTag_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4096))
_TmnxDot1agCfmMepControlSapTag_Type.__name__=_D
_TmnxDot1agCfmMepControlSapTag_Object=MibTableColumn
tmnxDot1agCfmMepControlSapTag=_TmnxDot1agCfmMepControlSapTag_Object((1,3,6,1,4,1,6527,6,2,2,2,11,1,1,1,2),_TmnxDot1agCfmMepControlSapTag_Type())
tmnxDot1agCfmMepControlSapTag.setMaxAccess(_F)
if mibBuilder.loadTexts:tmnxDot1agCfmMepControlSapTag.setStatus(_A)
_TmnxSASDot1agNotificationsPrefix_ObjectIdentity=ObjectIdentity
tmnxSASDot1agNotificationsPrefix=_TmnxSASDot1agNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,2,11,2))
_TmnxSASDot1agNotifications_ObjectIdentity=ObjectIdentity
tmnxSASDot1agNotifications=_TmnxSASDot1agNotifications_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,2,11,2,1))
dot1agCfmMepEntry.registerAugmentions((_B,_G))
tmnxDot1agCfmMepExtnEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())
tmnxSASDot1agCfmMepGroupV2v0=ObjectGroup((1,3,6,1,4,1,6527,6,2,2,1,7,2,1))
tmnxSASDot1agCfmMepGroupV2v0.setObjects((_B,_C))
if mibBuilder.loadTexts:tmnxSASDot1agCfmMepGroupV2v0.setStatus(_A)
tmnxSASDot1agCfmMepGroupV4v0=ObjectGroup((1,3,6,1,4,1,6527,6,2,2,1,7,2,2))
tmnxSASDot1agCfmMepGroupV4v0.setObjects(*((_B,_C),(_B,_H)))
if mibBuilder.loadTexts:tmnxSASDot1agCfmMepGroupV4v0.setStatus(_A)
tmnxSASDot1agCfmComplianceV2v0=ModuleCompliance((1,3,6,1,4,1,6527,6,2,2,1,7,1,2))
tmnxSASDot1agCfmComplianceV2v0.setObjects((_B,_I))
if mibBuilder.loadTexts:tmnxSASDot1agCfmComplianceV2v0.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'timetraSASIEEE8021CfmMIBModule':timetraSASIEEE8021CfmMIBModule,'tmnxSASDot1agMIBConformance':tmnxSASDot1agMIBConformance,'tmnxSASDot1agCfmCompliances':tmnxSASDot1agCfmCompliances,'tmnxSASDot1agCfmComplianceV2v0':tmnxSASDot1agCfmComplianceV2v0,'tmnxSASDot1agCfmGroups':tmnxSASDot1agCfmGroups,_I:tmnxSASDot1agCfmMepGroupV2v0,'tmnxSASDot1agCfmMepGroupV4v0':tmnxSASDot1agCfmMepGroupV4v0,'tmnxSASDot1agMIBObjs':tmnxSASDot1agMIBObjs,'tmnxSASDot1agCfmMep':tmnxSASDot1agCfmMep,'tmnxDot1agCfmMepExtnTable':tmnxDot1agCfmMepExtnTable,_G:tmnxDot1agCfmMepExtnEntry,_C:tmnxDot1agCfmMepSendAisOnPortDown,_H:tmnxDot1agCfmMepControlSapTag,'tmnxSASDot1agNotificationsPrefix':tmnxSASDot1agNotificationsPrefix,'tmnxSASDot1agNotifications':tmnxSASDot1agNotifications})