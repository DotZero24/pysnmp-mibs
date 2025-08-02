_c='pktcEnNcsGroup'
_b='pktcEnSigGroup'
_a='pktcEnNcsEndPntStatusReportCtrl'
_Z='pktcEnNcsEndPntLVMgmtMaintTimer'
_Y='pktcEnNcsEndPntLVMgmtResetTimer'
_X='pktcEnNcsEndPntLVMgmtPolicy'
_W='pktcEnEndPntFgnTestResults'
_V='pktcEnEndPntFgnTestValidity'
_U='pktcEnEndPntRunFgnPotTsts'
_T='pktcEnEndPntClrFgnPotTsts'
_S='pktcEnEndPntFgnPotDescr'
_R='pktcEnEndPntFgnPotSupport'
_Q='pktcEnNcsEndPntFaxDetection'
_P='pktcEnNcsEndPntHookState'
_O='pktcEnNcsEndPntQuarantineState'
_N='pktcEnNcsMinimumDtmfPlayout'
_M='pktcEnNcsEndPntConfigEntry'
_L='minutes'
_K='deprecated'
_J='TruthValue'
_I='ifIndex'
_H='IF-MIB'
_G='Unsigned32'
_F='Integer32'
_E='read-only'
_D='Bits'
_C='read-write'
_B='PKTC-EN-SIG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
pktcEnhancements,=mibBuilder.importSymbols('CLAB-DEF-MIB','pktcEnhancements')
ifIndex,=mibBuilder.importSymbols(_H,_I)
pktcNcsEndPntConfigEntry,=mibBuilder.importSymbols('PKTC-SIG-MIB','pktcNcsEndPntConfigEntry')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_D,'Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_J)
pktcEnSigMib=ModuleIdentity((1,3,6,1,4,1,4491,2,2,6,2))
if mibBuilder.loadTexts:pktcEnSigMib.setRevisions(('2005-01-28 00:00',))
_PktcEnSigMibObjects_ObjectIdentity=ObjectIdentity
pktcEnSigMibObjects=_PktcEnSigMibObjects_ObjectIdentity((1,3,6,1,4,1,4491,2,2,6,2,1))
_PktcEnSigDevConfigObjects_ObjectIdentity=ObjectIdentity
pktcEnSigDevConfigObjects=_PktcEnSigDevConfigObjects_ObjectIdentity((1,3,6,1,4,1,4491,2,2,6,2,1,1))
class _PktcEnNcsMinimumDtmfPlayout_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(40,100))
_PktcEnNcsMinimumDtmfPlayout_Type.__name__=_G
_PktcEnNcsMinimumDtmfPlayout_Object=MibScalar
pktcEnNcsMinimumDtmfPlayout=_PktcEnNcsMinimumDtmfPlayout_Object((1,3,6,1,4,1,4491,2,2,6,2,1,1,1),_PktcEnNcsMinimumDtmfPlayout_Type())
pktcEnNcsMinimumDtmfPlayout.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcEnNcsMinimumDtmfPlayout.setStatus(_A)
if mibBuilder.loadTexts:pktcEnNcsMinimumDtmfPlayout.setUnits('milliseconds')
_PktcEnNcsEndPntConfigObjects_ObjectIdentity=ObjectIdentity
pktcEnNcsEndPntConfigObjects=_PktcEnNcsEndPntConfigObjects_ObjectIdentity((1,3,6,1,4,1,4491,2,2,6,2,1,2))
_PktcEnNcsEndPntConfigTable_Object=MibTable
pktcEnNcsEndPntConfigTable=_PktcEnNcsEndPntConfigTable_Object((1,3,6,1,4,1,4491,2,2,6,2,1,2,1))
if mibBuilder.loadTexts:pktcEnNcsEndPntConfigTable.setStatus(_A)
_PktcEnNcsEndPntConfigEntry_Object=MibTableRow
pktcEnNcsEndPntConfigEntry=_PktcEnNcsEndPntConfigEntry_Object((1,3,6,1,4,1,4491,2,2,6,2,1,2,1,1))
if mibBuilder.loadTexts:pktcEnNcsEndPntConfigEntry.setStatus(_A)
class _PktcEnNcsEndPntQuarantineState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('normal',1),('notification',2),('lockstep',3),('extendedlockstep',4)))
_PktcEnNcsEndPntQuarantineState_Type.__name__=_F
_PktcEnNcsEndPntQuarantineState_Object=MibTableColumn
pktcEnNcsEndPntQuarantineState=_PktcEnNcsEndPntQuarantineState_Object((1,3,6,1,4,1,4491,2,2,6,2,1,2,1,1,1),_PktcEnNcsEndPntQuarantineState_Type())
pktcEnNcsEndPntQuarantineState.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcEnNcsEndPntQuarantineState.setStatus(_A)
class _PktcEnNcsEndPntHookState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('onHook',1),('onHookPlusNCSActivity',2),('offHook',3)))
_PktcEnNcsEndPntHookState_Type.__name__=_F
_PktcEnNcsEndPntHookState_Object=MibTableColumn
pktcEnNcsEndPntHookState=_PktcEnNcsEndPntHookState_Object((1,3,6,1,4,1,4491,2,2,6,2,1,2,1,1,2),_PktcEnNcsEndPntHookState_Type())
pktcEnNcsEndPntHookState.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcEnNcsEndPntHookState.setStatus(_A)
class _PktcEnNcsEndPntFaxDetection_Type(TruthValue):defaultValue=2
_PktcEnNcsEndPntFaxDetection_Type.__name__=_J
_PktcEnNcsEndPntFaxDetection_Object=MibTableColumn
pktcEnNcsEndPntFaxDetection=_PktcEnNcsEndPntFaxDetection_Object((1,3,6,1,4,1,4491,2,2,6,2,1,2,1,1,3),_PktcEnNcsEndPntFaxDetection_Type())
pktcEnNcsEndPntFaxDetection.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcEnNcsEndPntFaxDetection.setStatus(_A)
class _PktcEnNcsEndPntStatusReportCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unsupported',1),('reportActualStatus',2),('reportEndPointAsActive',3)))
_PktcEnNcsEndPntStatusReportCtrl_Type.__name__=_F
_PktcEnNcsEndPntStatusReportCtrl_Object=MibTableColumn
pktcEnNcsEndPntStatusReportCtrl=_PktcEnNcsEndPntStatusReportCtrl_Object((1,3,6,1,4,1,4491,2,2,6,2,1,2,1,1,4),_PktcEnNcsEndPntStatusReportCtrl_Type())
pktcEnNcsEndPntStatusReportCtrl.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcEnNcsEndPntStatusReportCtrl.setStatus(_K)
_PktcEnEndPntInfoTable_Object=MibTable
pktcEnEndPntInfoTable=_PktcEnEndPntInfoTable_Object((1,3,6,1,4,1,4491,2,2,6,2,1,2,2))
if mibBuilder.loadTexts:pktcEnEndPntInfoTable.setStatus(_A)
_PktcEnEndPntInfoTableEntry_Object=MibTableRow
pktcEnEndPntInfoTableEntry=_PktcEnEndPntInfoTableEntry_Object((1,3,6,1,4,1,4491,2,2,6,2,1,2,2,1))
pktcEnEndPntInfoTableEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:pktcEnEndPntInfoTableEntry.setStatus(_A)
class _PktcEnEndPntFgnPotSupport_Type(Bits):namedValues=NamedValues(*(('fgnPotDetection',0),('hazardousFgnPotDetection',1)))
_PktcEnEndPntFgnPotSupport_Type.__name__=_D
_PktcEnEndPntFgnPotSupport_Object=MibTableColumn
pktcEnEndPntFgnPotSupport=_PktcEnEndPntFgnPotSupport_Object((1,3,6,1,4,1,4491,2,2,6,2,1,2,2,1,1),_PktcEnEndPntFgnPotSupport_Type())
pktcEnEndPntFgnPotSupport.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcEnEndPntFgnPotSupport.setStatus(_A)
_PktcEnEndPntFgnPotDescr_Type=SnmpAdminString
_PktcEnEndPntFgnPotDescr_Object=MibTableColumn
pktcEnEndPntFgnPotDescr=_PktcEnEndPntFgnPotDescr_Object((1,3,6,1,4,1,4491,2,2,6,2,1,2,2,1,2),_PktcEnEndPntFgnPotDescr_Type())
pktcEnEndPntFgnPotDescr.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcEnEndPntFgnPotDescr.setStatus(_A)
class _PktcEnEndPntClrFgnPotTsts_Type(Bits):namedValues=NamedValues(*(('clrFgnPotentialResults',0),('clrHazardousPotResults',1)))
_PktcEnEndPntClrFgnPotTsts_Type.__name__=_D
_PktcEnEndPntClrFgnPotTsts_Object=MibTableColumn
pktcEnEndPntClrFgnPotTsts=_PktcEnEndPntClrFgnPotTsts_Object((1,3,6,1,4,1,4491,2,2,6,2,1,2,2,1,3),_PktcEnEndPntClrFgnPotTsts_Type())
pktcEnEndPntClrFgnPotTsts.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcEnEndPntClrFgnPotTsts.setStatus(_A)
class _PktcEnEndPntRunFgnPotTsts_Type(Bits):namedValues=NamedValues(*(('runFgnPotentialTsts',0),('runHazardousPotTsts',1)))
_PktcEnEndPntRunFgnPotTsts_Type.__name__=_D
_PktcEnEndPntRunFgnPotTsts_Object=MibTableColumn
pktcEnEndPntRunFgnPotTsts=_PktcEnEndPntRunFgnPotTsts_Object((1,3,6,1,4,1,4491,2,2,6,2,1,2,2,1,4),_PktcEnEndPntRunFgnPotTsts_Type())
pktcEnEndPntRunFgnPotTsts.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcEnEndPntRunFgnPotTsts.setStatus(_A)
class _PktcEnEndPntFgnTestValidity_Type(Bits):namedValues=NamedValues(*(('fgnPotTstValidity',0),('hazardousPotTstValidity',1)))
_PktcEnEndPntFgnTestValidity_Type.__name__=_D
_PktcEnEndPntFgnTestValidity_Object=MibTableColumn
pktcEnEndPntFgnTestValidity=_PktcEnEndPntFgnTestValidity_Object((1,3,6,1,4,1,4491,2,2,6,2,1,2,2,1,5),_PktcEnEndPntFgnTestValidity_Type())
pktcEnEndPntFgnTestValidity.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcEnEndPntFgnTestValidity.setStatus(_A)
class _PktcEnEndPntFgnTestResults_Type(Bits):namedValues=NamedValues(*(('fgnPotentialResults',0),('hazardousPotResults',1)))
_PktcEnEndPntFgnTestResults_Type.__name__=_D
_PktcEnEndPntFgnTestResults_Object=MibTableColumn
pktcEnEndPntFgnTestResults=_PktcEnEndPntFgnTestResults_Object((1,3,6,1,4,1,4491,2,2,6,2,1,2,2,1,6),_PktcEnEndPntFgnTestResults_Type())
pktcEnEndPntFgnTestResults.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcEnEndPntFgnTestResults.setStatus(_A)
_PktcEnNcsEndPntLVMgmtTable_Object=MibTable
pktcEnNcsEndPntLVMgmtTable=_PktcEnNcsEndPntLVMgmtTable_Object((1,3,6,1,4,1,4491,2,2,6,2,1,2,3))
if mibBuilder.loadTexts:pktcEnNcsEndPntLVMgmtTable.setStatus(_A)
_PktcEnNcsEndPntLVMgmtTableEntry_Object=MibTableRow
pktcEnNcsEndPntLVMgmtTableEntry=_PktcEnNcsEndPntLVMgmtTableEntry_Object((1,3,6,1,4,1,4491,2,2,6,2,1,2,3,1))
pktcEnNcsEndPntLVMgmtTableEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:pktcEnNcsEndPntLVMgmtTableEntry.setStatus(_A)
class _PktcEnNcsEndPntLVMgmtPolicy_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('voltageAtAllTimes',1),('voltageUnlessRFQAMabsent',2),('voltageBasedOnServiceOrTimers',3),('voltageBasedOnService',4)))
_PktcEnNcsEndPntLVMgmtPolicy_Type.__name__=_F
_PktcEnNcsEndPntLVMgmtPolicy_Object=MibTableColumn
pktcEnNcsEndPntLVMgmtPolicy=_PktcEnNcsEndPntLVMgmtPolicy_Object((1,3,6,1,4,1,4491,2,2,6,2,1,2,3,1,1),_PktcEnNcsEndPntLVMgmtPolicy_Type())
pktcEnNcsEndPntLVMgmtPolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcEnNcsEndPntLVMgmtPolicy.setStatus(_A)
class _PktcEnNcsEndPntLVMgmtResetTimer_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1440))
_PktcEnNcsEndPntLVMgmtResetTimer_Type.__name__=_G
_PktcEnNcsEndPntLVMgmtResetTimer_Object=MibTableColumn
pktcEnNcsEndPntLVMgmtResetTimer=_PktcEnNcsEndPntLVMgmtResetTimer_Object((1,3,6,1,4,1,4491,2,2,6,2,1,2,3,1,2),_PktcEnNcsEndPntLVMgmtResetTimer_Type())
pktcEnNcsEndPntLVMgmtResetTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcEnNcsEndPntLVMgmtResetTimer.setStatus(_A)
if mibBuilder.loadTexts:pktcEnNcsEndPntLVMgmtResetTimer.setUnits(_L)
class _PktcEnNcsEndPntLVMgmtMaintTimer_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1440))
_PktcEnNcsEndPntLVMgmtMaintTimer_Type.__name__=_G
_PktcEnNcsEndPntLVMgmtMaintTimer_Object=MibTableColumn
pktcEnNcsEndPntLVMgmtMaintTimer=_PktcEnNcsEndPntLVMgmtMaintTimer_Object((1,3,6,1,4,1,4491,2,2,6,2,1,2,3,1,3),_PktcEnNcsEndPntLVMgmtMaintTimer_Type())
pktcEnNcsEndPntLVMgmtMaintTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcEnNcsEndPntLVMgmtMaintTimer.setStatus(_A)
if mibBuilder.loadTexts:pktcEnNcsEndPntLVMgmtMaintTimer.setUnits(_L)
_PktcEnSigEndPntConfigObjects_ObjectIdentity=ObjectIdentity
pktcEnSigEndPntConfigObjects=_PktcEnSigEndPntConfigObjects_ObjectIdentity((1,3,6,1,4,1,4491,2,2,6,2,1,3))
_PktcEnDcsEndPntConfigObjects_ObjectIdentity=ObjectIdentity
pktcEnDcsEndPntConfigObjects=_PktcEnDcsEndPntConfigObjects_ObjectIdentity((1,3,6,1,4,1,4491,2,2,6,2,1,4))
_PktcEnSigNotificationPrefix_ObjectIdentity=ObjectIdentity
pktcEnSigNotificationPrefix=_PktcEnSigNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,4491,2,2,6,2,2))
_PktcEnSigNotification_ObjectIdentity=ObjectIdentity
pktcEnSigNotification=_PktcEnSigNotification_ObjectIdentity((1,3,6,1,4,1,4491,2,2,6,2,2,0))
_PktcEnSigConformance_ObjectIdentity=ObjectIdentity
pktcEnSigConformance=_PktcEnSigConformance_ObjectIdentity((1,3,6,1,4,1,4491,2,2,6,2,3))
_PktcEnSigCompliances_ObjectIdentity=ObjectIdentity
pktcEnSigCompliances=_PktcEnSigCompliances_ObjectIdentity((1,3,6,1,4,1,4491,2,2,6,2,3,1))
_PktcEnSigGroups_ObjectIdentity=ObjectIdentity
pktcEnSigGroups=_PktcEnSigGroups_ObjectIdentity((1,3,6,1,4,1,4491,2,2,6,2,3,2))
pktcNcsEndPntConfigEntry.registerAugmentions((_B,_M))
pktcEnNcsEndPntConfigEntry.setIndexNames(*pktcNcsEndPntConfigEntry.getIndexNames())
pktcEnSigGroup=ObjectGroup((1,3,6,1,4,1,4491,2,2,6,2,3,2,1))
pktcEnSigGroup.setObjects((_B,_N))
if mibBuilder.loadTexts:pktcEnSigGroup.setStatus(_A)
pktcEnNcsGroup=ObjectGroup((1,3,6,1,4,1,4491,2,2,6,2,3,2,2))
pktcEnNcsGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:pktcEnNcsGroup.setStatus(_A)
pktcEnNcsLVMgmtGroup=ObjectGroup((1,3,6,1,4,1,4491,2,2,6,2,3,2,3))
pktcEnNcsLVMgmtGroup.setObjects(*((_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:pktcEnNcsLVMgmtGroup.setStatus(_A)
pktcEnNcsDeprecatedGroup=ObjectGroup((1,3,6,1,4,1,4491,2,2,6,2,3,2,4))
pktcEnNcsDeprecatedGroup.setObjects((_B,_a))
if mibBuilder.loadTexts:pktcEnNcsDeprecatedGroup.setStatus(_K)
pktcEnSigBasicCompliance=ModuleCompliance((1,3,6,1,4,1,4491,2,2,6,2,3,1,1))
pktcEnSigBasicCompliance.setObjects(*((_B,_b),(_B,_c)))
if mibBuilder.loadTexts:pktcEnSigBasicCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'pktcEnSigMib':pktcEnSigMib,'pktcEnSigMibObjects':pktcEnSigMibObjects,'pktcEnSigDevConfigObjects':pktcEnSigDevConfigObjects,_N:pktcEnNcsMinimumDtmfPlayout,'pktcEnNcsEndPntConfigObjects':pktcEnNcsEndPntConfigObjects,'pktcEnNcsEndPntConfigTable':pktcEnNcsEndPntConfigTable,_M:pktcEnNcsEndPntConfigEntry,_O:pktcEnNcsEndPntQuarantineState,_P:pktcEnNcsEndPntHookState,_Q:pktcEnNcsEndPntFaxDetection,_a:pktcEnNcsEndPntStatusReportCtrl,'pktcEnEndPntInfoTable':pktcEnEndPntInfoTable,'pktcEnEndPntInfoTableEntry':pktcEnEndPntInfoTableEntry,_R:pktcEnEndPntFgnPotSupport,_S:pktcEnEndPntFgnPotDescr,_T:pktcEnEndPntClrFgnPotTsts,_U:pktcEnEndPntRunFgnPotTsts,_V:pktcEnEndPntFgnTestValidity,_W:pktcEnEndPntFgnTestResults,'pktcEnNcsEndPntLVMgmtTable':pktcEnNcsEndPntLVMgmtTable,'pktcEnNcsEndPntLVMgmtTableEntry':pktcEnNcsEndPntLVMgmtTableEntry,_X:pktcEnNcsEndPntLVMgmtPolicy,_Y:pktcEnNcsEndPntLVMgmtResetTimer,_Z:pktcEnNcsEndPntLVMgmtMaintTimer,'pktcEnSigEndPntConfigObjects':pktcEnSigEndPntConfigObjects,'pktcEnDcsEndPntConfigObjects':pktcEnDcsEndPntConfigObjects,'pktcEnSigNotificationPrefix':pktcEnSigNotificationPrefix,'pktcEnSigNotification':pktcEnSigNotification,'pktcEnSigConformance':pktcEnSigConformance,'pktcEnSigCompliances':pktcEnSigCompliances,'pktcEnSigBasicCompliance':pktcEnSigBasicCompliance,'pktcEnSigGroups':pktcEnSigGroups,_b:pktcEnSigGroup,_c:pktcEnNcsGroup,'pktcEnNcsLVMgmtGroup':pktcEnNcsLVMgmtGroup,'pktcEnNcsDeprecatedGroup':pktcEnNcsDeprecatedGroup})