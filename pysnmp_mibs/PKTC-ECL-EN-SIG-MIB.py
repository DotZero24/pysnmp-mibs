_d='pktcEnNcsGroup'
_c='pktcEnSigGroup'
_b='pktcEnNcsEndPntStatusReportCtrl'
_a='pktcEnNcsEndPntLVMgmtMaintTimer'
_Z='pktcEnNcsEndPntLVMgmtResetTimer'
_Y='pktcEnNcsEndPntLVMgmtPolicy'
_X='pktcEnEndPntFgnTestResults'
_W='pktcEnEndPntFgnTestValidity'
_V='pktcEnEndPntRunFgnPotTsts'
_U='pktcEnEndPntClrFgnPotTsts'
_T='pktcEnEndPntFgnPotDescr'
_S='pktcEnEndPntFgnPotSupport'
_R='pktcEnNcsEndPntFaxDetection'
_Q='pktcEnNcsEndPntHookState'
_P='pktcEnNcsEndPntQuarantineState'
_O='pktcEnNcsMinimumDtmfPlayout'
_N='pktcEnNcsEndPntConfigEntry'
_M='minutes'
_L='deprecated'
_K='read-create'
_J='TruthValue'
_I='ifIndex'
_H='IF-MIB'
_G='Unsigned32'
_F='Integer32'
_E='read-only'
_D='read-write'
_C='Bits'
_B='PKTC-ECL-EN-SIG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
pktcEclEnhancements,=mibBuilder.importSymbols('ECL-DEF-MIB','pktcEclEnhancements')
ifIndex,=mibBuilder.importSymbols(_H,_I)
pktcNcsEndPntConfigEntry,=mibBuilder.importSymbols('PKTC-EXCENTIS-SIG-MIB','pktcNcsEndPntConfigEntry')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_C,'Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_J)
pktcEclEnSigMib=ModuleIdentity((1,3,6,1,4,1,24624,2,2,6,2))
if mibBuilder.loadTexts:pktcEclEnSigMib.setRevisions(('2007-05-25 00:00','2005-01-28 00:00'))
_PktcEnSigMibObjects_ObjectIdentity=ObjectIdentity
pktcEnSigMibObjects=_PktcEnSigMibObjects_ObjectIdentity((1,3,6,1,4,1,24624,2,2,6,2,1))
_PktcEnSigDevConfigObjects_ObjectIdentity=ObjectIdentity
pktcEnSigDevConfigObjects=_PktcEnSigDevConfigObjects_ObjectIdentity((1,3,6,1,4,1,24624,2,2,6,2,1,1))
class _PktcEnNcsMinimumDtmfPlayout_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(40,100))
_PktcEnNcsMinimumDtmfPlayout_Type.__name__=_G
_PktcEnNcsMinimumDtmfPlayout_Object=MibScalar
pktcEnNcsMinimumDtmfPlayout=_PktcEnNcsMinimumDtmfPlayout_Object((1,3,6,1,4,1,24624,2,2,6,2,1,1,1),_PktcEnNcsMinimumDtmfPlayout_Type())
pktcEnNcsMinimumDtmfPlayout.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcEnNcsMinimumDtmfPlayout.setStatus(_A)
if mibBuilder.loadTexts:pktcEnNcsMinimumDtmfPlayout.setUnits('milliseconds')
_PktcEnNcsEndPntConfigObjects_ObjectIdentity=ObjectIdentity
pktcEnNcsEndPntConfigObjects=_PktcEnNcsEndPntConfigObjects_ObjectIdentity((1,3,6,1,4,1,24624,2,2,6,2,1,2))
_PktcEnNcsEndPntConfigTable_Object=MibTable
pktcEnNcsEndPntConfigTable=_PktcEnNcsEndPntConfigTable_Object((1,3,6,1,4,1,24624,2,2,6,2,1,2,1))
if mibBuilder.loadTexts:pktcEnNcsEndPntConfigTable.setStatus(_A)
_PktcEnNcsEndPntConfigEntry_Object=MibTableRow
pktcEnNcsEndPntConfigEntry=_PktcEnNcsEndPntConfigEntry_Object((1,3,6,1,4,1,24624,2,2,6,2,1,2,1,1))
if mibBuilder.loadTexts:pktcEnNcsEndPntConfigEntry.setStatus(_A)
class _PktcEnNcsEndPntQuarantineState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('normal',1),('notification',2),('lockstep',3),('extendedlockstep',4)))
_PktcEnNcsEndPntQuarantineState_Type.__name__=_F
_PktcEnNcsEndPntQuarantineState_Object=MibTableColumn
pktcEnNcsEndPntQuarantineState=_PktcEnNcsEndPntQuarantineState_Object((1,3,6,1,4,1,24624,2,2,6,2,1,2,1,1,1),_PktcEnNcsEndPntQuarantineState_Type())
pktcEnNcsEndPntQuarantineState.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcEnNcsEndPntQuarantineState.setStatus(_A)
class _PktcEnNcsEndPntHookState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('onHook',1),('onHookPlusNCSActivity',2),('offHook',3)))
_PktcEnNcsEndPntHookState_Type.__name__=_F
_PktcEnNcsEndPntHookState_Object=MibTableColumn
pktcEnNcsEndPntHookState=_PktcEnNcsEndPntHookState_Object((1,3,6,1,4,1,24624,2,2,6,2,1,2,1,1,2),_PktcEnNcsEndPntHookState_Type())
pktcEnNcsEndPntHookState.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcEnNcsEndPntHookState.setStatus(_A)
class _PktcEnNcsEndPntFaxDetection_Type(TruthValue):defaultValue=2
_PktcEnNcsEndPntFaxDetection_Type.__name__=_J
_PktcEnNcsEndPntFaxDetection_Object=MibTableColumn
pktcEnNcsEndPntFaxDetection=_PktcEnNcsEndPntFaxDetection_Object((1,3,6,1,4,1,24624,2,2,6,2,1,2,1,1,3),_PktcEnNcsEndPntFaxDetection_Type())
pktcEnNcsEndPntFaxDetection.setMaxAccess(_K)
if mibBuilder.loadTexts:pktcEnNcsEndPntFaxDetection.setStatus(_A)
class _PktcEnNcsEndPntStatusReportCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unsupported',1),('reportActualStatus',2),('reportEndPointAsActive',3)))
_PktcEnNcsEndPntStatusReportCtrl_Type.__name__=_F
_PktcEnNcsEndPntStatusReportCtrl_Object=MibTableColumn
pktcEnNcsEndPntStatusReportCtrl=_PktcEnNcsEndPntStatusReportCtrl_Object((1,3,6,1,4,1,24624,2,2,6,2,1,2,1,1,4),_PktcEnNcsEndPntStatusReportCtrl_Type())
pktcEnNcsEndPntStatusReportCtrl.setMaxAccess(_K)
if mibBuilder.loadTexts:pktcEnNcsEndPntStatusReportCtrl.setStatus(_L)
_PktcEnEndPntInfoTable_Object=MibTable
pktcEnEndPntInfoTable=_PktcEnEndPntInfoTable_Object((1,3,6,1,4,1,24624,2,2,6,2,1,2,2))
if mibBuilder.loadTexts:pktcEnEndPntInfoTable.setStatus(_A)
_PktcEnEndPntInfoEntry_Object=MibTableRow
pktcEnEndPntInfoEntry=_PktcEnEndPntInfoEntry_Object((1,3,6,1,4,1,24624,2,2,6,2,1,2,2,1))
pktcEnEndPntInfoEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:pktcEnEndPntInfoEntry.setStatus(_A)
class _PktcEnEndPntFgnPotSupport_Type(Bits):namedValues=NamedValues(*(('fgnPotDetection',0),('hazardousFgnPotDetection',1)))
_PktcEnEndPntFgnPotSupport_Type.__name__=_C
_PktcEnEndPntFgnPotSupport_Object=MibTableColumn
pktcEnEndPntFgnPotSupport=_PktcEnEndPntFgnPotSupport_Object((1,3,6,1,4,1,24624,2,2,6,2,1,2,2,1,1),_PktcEnEndPntFgnPotSupport_Type())
pktcEnEndPntFgnPotSupport.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcEnEndPntFgnPotSupport.setStatus(_A)
_PktcEnEndPntFgnPotDescr_Type=SnmpAdminString
_PktcEnEndPntFgnPotDescr_Object=MibTableColumn
pktcEnEndPntFgnPotDescr=_PktcEnEndPntFgnPotDescr_Object((1,3,6,1,4,1,24624,2,2,6,2,1,2,2,1,2),_PktcEnEndPntFgnPotDescr_Type())
pktcEnEndPntFgnPotDescr.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcEnEndPntFgnPotDescr.setStatus(_A)
class _PktcEnEndPntClrFgnPotTsts_Type(Bits):namedValues=NamedValues(*(('clrFgnPotentialResults',0),('clrHazardousPotResults',1)))
_PktcEnEndPntClrFgnPotTsts_Type.__name__=_C
_PktcEnEndPntClrFgnPotTsts_Object=MibTableColumn
pktcEnEndPntClrFgnPotTsts=_PktcEnEndPntClrFgnPotTsts_Object((1,3,6,1,4,1,24624,2,2,6,2,1,2,2,1,3),_PktcEnEndPntClrFgnPotTsts_Type())
pktcEnEndPntClrFgnPotTsts.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcEnEndPntClrFgnPotTsts.setStatus(_A)
class _PktcEnEndPntRunFgnPotTsts_Type(Bits):namedValues=NamedValues(*(('runFgnPotentialTsts',0),('runHazardousPotTsts',1)))
_PktcEnEndPntRunFgnPotTsts_Type.__name__=_C
_PktcEnEndPntRunFgnPotTsts_Object=MibTableColumn
pktcEnEndPntRunFgnPotTsts=_PktcEnEndPntRunFgnPotTsts_Object((1,3,6,1,4,1,24624,2,2,6,2,1,2,2,1,4),_PktcEnEndPntRunFgnPotTsts_Type())
pktcEnEndPntRunFgnPotTsts.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcEnEndPntRunFgnPotTsts.setStatus(_A)
class _PktcEnEndPntFgnTestValidity_Type(Bits):namedValues=NamedValues(*(('fgnPotTstValidity',0),('hazardousPotTstValidity',1)))
_PktcEnEndPntFgnTestValidity_Type.__name__=_C
_PktcEnEndPntFgnTestValidity_Object=MibTableColumn
pktcEnEndPntFgnTestValidity=_PktcEnEndPntFgnTestValidity_Object((1,3,6,1,4,1,24624,2,2,6,2,1,2,2,1,5),_PktcEnEndPntFgnTestValidity_Type())
pktcEnEndPntFgnTestValidity.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcEnEndPntFgnTestValidity.setStatus(_A)
class _PktcEnEndPntFgnTestResults_Type(Bits):namedValues=NamedValues(*(('fgnPotentialResults',0),('hazardousPotResults',1)))
_PktcEnEndPntFgnTestResults_Type.__name__=_C
_PktcEnEndPntFgnTestResults_Object=MibTableColumn
pktcEnEndPntFgnTestResults=_PktcEnEndPntFgnTestResults_Object((1,3,6,1,4,1,24624,2,2,6,2,1,2,2,1,6),_PktcEnEndPntFgnTestResults_Type())
pktcEnEndPntFgnTestResults.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcEnEndPntFgnTestResults.setStatus(_A)
_PktcEnNcsEndPntLVMgmtTable_Object=MibTable
pktcEnNcsEndPntLVMgmtTable=_PktcEnNcsEndPntLVMgmtTable_Object((1,3,6,1,4,1,24624,2,2,6,2,1,2,3))
if mibBuilder.loadTexts:pktcEnNcsEndPntLVMgmtTable.setStatus(_A)
_PktcEnNcsEndPntLVMgmtEntry_Object=MibTableRow
pktcEnNcsEndPntLVMgmtEntry=_PktcEnNcsEndPntLVMgmtEntry_Object((1,3,6,1,4,1,24624,2,2,6,2,1,2,3,1))
pktcEnNcsEndPntLVMgmtEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:pktcEnNcsEndPntLVMgmtEntry.setStatus(_A)
class _PktcEnNcsEndPntLVMgmtPolicy_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('voltageAtAllTimes',1),('voltageUnlessRFQAMabsent',2),('voltageBasedOnServiceOrTimers',3),('voltageBasedOnService',4)))
_PktcEnNcsEndPntLVMgmtPolicy_Type.__name__=_F
_PktcEnNcsEndPntLVMgmtPolicy_Object=MibTableColumn
pktcEnNcsEndPntLVMgmtPolicy=_PktcEnNcsEndPntLVMgmtPolicy_Object((1,3,6,1,4,1,24624,2,2,6,2,1,2,3,1,1),_PktcEnNcsEndPntLVMgmtPolicy_Type())
pktcEnNcsEndPntLVMgmtPolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcEnNcsEndPntLVMgmtPolicy.setStatus(_A)
class _PktcEnNcsEndPntLVMgmtResetTimer_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1440))
_PktcEnNcsEndPntLVMgmtResetTimer_Type.__name__=_G
_PktcEnNcsEndPntLVMgmtResetTimer_Object=MibTableColumn
pktcEnNcsEndPntLVMgmtResetTimer=_PktcEnNcsEndPntLVMgmtResetTimer_Object((1,3,6,1,4,1,24624,2,2,6,2,1,2,3,1,2),_PktcEnNcsEndPntLVMgmtResetTimer_Type())
pktcEnNcsEndPntLVMgmtResetTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcEnNcsEndPntLVMgmtResetTimer.setStatus(_A)
if mibBuilder.loadTexts:pktcEnNcsEndPntLVMgmtResetTimer.setUnits(_M)
class _PktcEnNcsEndPntLVMgmtMaintTimer_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1440))
_PktcEnNcsEndPntLVMgmtMaintTimer_Type.__name__=_G
_PktcEnNcsEndPntLVMgmtMaintTimer_Object=MibTableColumn
pktcEnNcsEndPntLVMgmtMaintTimer=_PktcEnNcsEndPntLVMgmtMaintTimer_Object((1,3,6,1,4,1,24624,2,2,6,2,1,2,3,1,3),_PktcEnNcsEndPntLVMgmtMaintTimer_Type())
pktcEnNcsEndPntLVMgmtMaintTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcEnNcsEndPntLVMgmtMaintTimer.setStatus(_A)
if mibBuilder.loadTexts:pktcEnNcsEndPntLVMgmtMaintTimer.setUnits(_M)
_PktcEnSigEndPntConfigObjects_ObjectIdentity=ObjectIdentity
pktcEnSigEndPntConfigObjects=_PktcEnSigEndPntConfigObjects_ObjectIdentity((1,3,6,1,4,1,24624,2,2,6,2,1,3))
_PktcEnDcsEndPntConfigObjects_ObjectIdentity=ObjectIdentity
pktcEnDcsEndPntConfigObjects=_PktcEnDcsEndPntConfigObjects_ObjectIdentity((1,3,6,1,4,1,24624,2,2,6,2,1,4))
_PktcEnSigNotificationPrefix_ObjectIdentity=ObjectIdentity
pktcEnSigNotificationPrefix=_PktcEnSigNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,24624,2,2,6,2,2))
_PktcEnSigNotification_ObjectIdentity=ObjectIdentity
pktcEnSigNotification=_PktcEnSigNotification_ObjectIdentity((1,3,6,1,4,1,24624,2,2,6,2,2,0))
_PktcEnSigConformance_ObjectIdentity=ObjectIdentity
pktcEnSigConformance=_PktcEnSigConformance_ObjectIdentity((1,3,6,1,4,1,24624,2,2,6,2,3))
_PktcEnSigCompliances_ObjectIdentity=ObjectIdentity
pktcEnSigCompliances=_PktcEnSigCompliances_ObjectIdentity((1,3,6,1,4,1,24624,2,2,6,2,3,1))
_PktcEnSigGroups_ObjectIdentity=ObjectIdentity
pktcEnSigGroups=_PktcEnSigGroups_ObjectIdentity((1,3,6,1,4,1,24624,2,2,6,2,3,2))
pktcNcsEndPntConfigEntry.registerAugmentions((_B,_N))
pktcEnNcsEndPntConfigEntry.setIndexNames(*pktcNcsEndPntConfigEntry.getIndexNames())
pktcEnSigGroup=ObjectGroup((1,3,6,1,4,1,24624,2,2,6,2,3,2,1))
pktcEnSigGroup.setObjects((_B,_O))
if mibBuilder.loadTexts:pktcEnSigGroup.setStatus(_A)
pktcEnNcsGroup=ObjectGroup((1,3,6,1,4,1,24624,2,2,6,2,3,2,2))
pktcEnNcsGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:pktcEnNcsGroup.setStatus(_A)
pktcEnNcsLVMgmtGroup=ObjectGroup((1,3,6,1,4,1,24624,2,2,6,2,3,2,3))
pktcEnNcsLVMgmtGroup.setObjects(*((_B,_Y),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:pktcEnNcsLVMgmtGroup.setStatus(_A)
pktcEnNcsDeprecatedGroup=ObjectGroup((1,3,6,1,4,1,24624,2,2,6,2,3,2,4))
pktcEnNcsDeprecatedGroup.setObjects((_B,_b))
if mibBuilder.loadTexts:pktcEnNcsDeprecatedGroup.setStatus(_L)
pktcSigBasicCompliance=ModuleCompliance((1,3,6,1,4,1,24624,2,2,6,2,3,1,1))
pktcSigBasicCompliance.setObjects(*((_B,_c),(_B,_d)))
if mibBuilder.loadTexts:pktcSigBasicCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'pktcEclEnSigMib':pktcEclEnSigMib,'pktcEnSigMibObjects':pktcEnSigMibObjects,'pktcEnSigDevConfigObjects':pktcEnSigDevConfigObjects,_O:pktcEnNcsMinimumDtmfPlayout,'pktcEnNcsEndPntConfigObjects':pktcEnNcsEndPntConfigObjects,'pktcEnNcsEndPntConfigTable':pktcEnNcsEndPntConfigTable,_N:pktcEnNcsEndPntConfigEntry,_P:pktcEnNcsEndPntQuarantineState,_Q:pktcEnNcsEndPntHookState,_R:pktcEnNcsEndPntFaxDetection,_b:pktcEnNcsEndPntStatusReportCtrl,'pktcEnEndPntInfoTable':pktcEnEndPntInfoTable,'pktcEnEndPntInfoEntry':pktcEnEndPntInfoEntry,_S:pktcEnEndPntFgnPotSupport,_T:pktcEnEndPntFgnPotDescr,_U:pktcEnEndPntClrFgnPotTsts,_V:pktcEnEndPntRunFgnPotTsts,_W:pktcEnEndPntFgnTestValidity,_X:pktcEnEndPntFgnTestResults,'pktcEnNcsEndPntLVMgmtTable':pktcEnNcsEndPntLVMgmtTable,'pktcEnNcsEndPntLVMgmtEntry':pktcEnNcsEndPntLVMgmtEntry,_Y:pktcEnNcsEndPntLVMgmtPolicy,_Z:pktcEnNcsEndPntLVMgmtResetTimer,_a:pktcEnNcsEndPntLVMgmtMaintTimer,'pktcEnSigEndPntConfigObjects':pktcEnSigEndPntConfigObjects,'pktcEnDcsEndPntConfigObjects':pktcEnDcsEndPntConfigObjects,'pktcEnSigNotificationPrefix':pktcEnSigNotificationPrefix,'pktcEnSigNotification':pktcEnSigNotification,'pktcEnSigConformance':pktcEnSigConformance,'pktcEnSigCompliances':pktcEnSigCompliances,'pktcSigBasicCompliance':pktcSigBasicCompliance,'pktcEnSigGroups':pktcEnSigGroups,_c:pktcEnSigGroup,_d:pktcEnNcsGroup,'pktcEnNcsLVMgmtGroup':pktcEnNcsLVMgmtGroup,'pktcEnNcsDeprecatedGroup':pktcEnNcsDeprecatedGroup})