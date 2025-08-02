_V='wfPgmReXmitParityTgSeqNum'
_U='wfPgmReXmitSelectiveSeqNum'
_T='wfPgmReXmitGlobalId'
_S='wfPgmReXmitSourcePort'
_R='wfPgmReXmitGroup'
_Q='wfPgmReXmitSource'
_P='wfPgmSessionGlobalId'
_O='wfPgmSessionSourcePort'
_N='wfPgmSessionGroup'
_M='wfPgmSessionSource'
_L='wfPgmIfCct'
_K='notpres'
_J='deleted'
_I='created'
_H='disabled'
_G='enabled'
_F='OctetString'
_E='Wellfleet-PGM-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
wfPgmGroup,=mibBuilder.importSymbols('Wellfleet-COMMON-MIB','wfPgmGroup')
_WfPgm_ObjectIdentity=ObjectIdentity
wfPgm=_WfPgm_ObjectIdentity((1,3,6,1,4,1,18,3,5,28,1))
class _WfPgmCreate_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_WfPgmCreate_Type.__name__=_C
_WfPgmCreate_Object=MibScalar
wfPgmCreate=_WfPgmCreate_Object((1,3,6,1,4,1,18,3,5,28,1,1),_WfPgmCreate_Type())
wfPgmCreate.setMaxAccess(_D)
if mibBuilder.loadTexts:wfPgmCreate.setStatus(_A)
class _WfPgmEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_WfPgmEnable_Type.__name__=_C
_WfPgmEnable_Object=MibScalar
wfPgmEnable=_WfPgmEnable_Object((1,3,6,1,4,1,18,3,5,28,1,2),_WfPgmEnable_Type())
wfPgmEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:wfPgmEnable.setStatus(_A)
class _WfPgmState_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('up',1),('down',2),('init',3),(_K,4)))
_WfPgmState_Type.__name__=_C
_WfPgmState_Object=MibScalar
wfPgmState=_WfPgmState_Object((1,3,6,1,4,1,18,3,5,28,1,3),_WfPgmState_Type())
wfPgmState.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmState.setStatus(_A)
_WfPgmDebug_Type=Integer32
_WfPgmDebug_Object=MibScalar
wfPgmDebug=_WfPgmDebug_Object((1,3,6,1,4,1,18,3,5,28,1,4),_WfPgmDebug_Type())
wfPgmDebug.setMaxAccess(_D)
if mibBuilder.loadTexts:wfPgmDebug.setStatus(_A)
class _WfPgmSessionLifeTime_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_WfPgmSessionLifeTime_Type.__name__=_C
_WfPgmSessionLifeTime_Object=MibScalar
wfPgmSessionLifeTime=_WfPgmSessionLifeTime_Object((1,3,6,1,4,1,18,3,5,28,1,5),_WfPgmSessionLifeTime_Type())
wfPgmSessionLifeTime.setMaxAccess(_D)
if mibBuilder.loadTexts:wfPgmSessionLifeTime.setStatus(_A)
class _WfPgmNnakGenerate_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_WfPgmNnakGenerate_Type.__name__=_C
_WfPgmNnakGenerate_Object=MibScalar
wfPgmNnakGenerate=_WfPgmNnakGenerate_Object((1,3,6,1,4,1,18,3,5,28,1,6),_WfPgmNnakGenerate_Type())
wfPgmNnakGenerate.setMaxAccess(_D)
if mibBuilder.loadTexts:wfPgmNnakGenerate.setStatus(_A)
class _WfPgmMaxReXmitStates_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_WfPgmMaxReXmitStates_Type.__name__=_C
_WfPgmMaxReXmitStates_Object=MibScalar
wfPgmMaxReXmitStates=_WfPgmMaxReXmitStates_Object((1,3,6,1,4,1,18,3,5,28,1,7),_WfPgmMaxReXmitStates_Type())
wfPgmMaxReXmitStates.setMaxAccess(_D)
if mibBuilder.loadTexts:wfPgmMaxReXmitStates.setStatus(_A)
_WfPgmTotalReXmitStates_Type=Gauge32
_WfPgmTotalReXmitStates_Object=MibScalar
wfPgmTotalReXmitStates=_WfPgmTotalReXmitStates_Object((1,3,6,1,4,1,18,3,5,28,1,8),_WfPgmTotalReXmitStates_Type())
wfPgmTotalReXmitStates.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmTotalReXmitStates.setStatus(_A)
class _WfPgmMaxSessions_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_WfPgmMaxSessions_Type.__name__=_C
_WfPgmMaxSessions_Object=MibScalar
wfPgmMaxSessions=_WfPgmMaxSessions_Object((1,3,6,1,4,1,18,3,5,28,1,9),_WfPgmMaxSessions_Type())
wfPgmMaxSessions.setMaxAccess(_D)
if mibBuilder.loadTexts:wfPgmMaxSessions.setStatus(_A)
_WfPgmTotalSessions_Type=Gauge32
_WfPgmTotalSessions_Object=MibScalar
wfPgmTotalSessions=_WfPgmTotalSessions_Object((1,3,6,1,4,1,18,3,5,28,1,10),_WfPgmTotalSessions_Type())
wfPgmTotalSessions.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmTotalSessions.setStatus(_A)
_WfPgmTotalReXmitStatesTimedOut_Type=Gauge32
_WfPgmTotalReXmitStatesTimedOut_Object=MibScalar
wfPgmTotalReXmitStatesTimedOut=_WfPgmTotalReXmitStatesTimedOut_Object((1,3,6,1,4,1,18,3,5,28,1,11),_WfPgmTotalReXmitStatesTimedOut_Type())
wfPgmTotalReXmitStatesTimedOut.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmTotalReXmitStatesTimedOut.setStatus(_A)
_WfPgmTotalUniqueNaks_Type=Gauge32
_WfPgmTotalUniqueNaks_Object=MibScalar
wfPgmTotalUniqueNaks=_WfPgmTotalUniqueNaks_Object((1,3,6,1,4,1,18,3,5,28,1,12),_WfPgmTotalUniqueNaks_Type())
wfPgmTotalUniqueNaks.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmTotalUniqueNaks.setStatus(_A)
_WfPgmTotalUniqueParityNaks_Type=Gauge32
_WfPgmTotalUniqueParityNaks_Object=MibScalar
wfPgmTotalUniqueParityNaks=_WfPgmTotalUniqueParityNaks_Object((1,3,6,1,4,1,18,3,5,28,1,13),_WfPgmTotalUniqueParityNaks_Type())
wfPgmTotalUniqueParityNaks.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmTotalUniqueParityNaks.setStatus(_A)
class _WfPgmMaxNakRate_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_WfPgmMaxNakRate_Type.__name__=_C
_WfPgmMaxNakRate_Object=MibScalar
wfPgmMaxNakRate=_WfPgmMaxNakRate_Object((1,3,6,1,4,1,18,3,5,28,1,14),_WfPgmMaxNakRate_Type())
wfPgmMaxNakRate.setMaxAccess(_D)
if mibBuilder.loadTexts:wfPgmMaxNakRate.setStatus(_A)
_WfPgmIfTable_Object=MibTable
wfPgmIfTable=_WfPgmIfTable_Object((1,3,6,1,4,1,18,3,5,28,2))
if mibBuilder.loadTexts:wfPgmIfTable.setStatus(_A)
_WfPgmIfEntry_Object=MibTableRow
wfPgmIfEntry=_WfPgmIfEntry_Object((1,3,6,1,4,1,18,3,5,28,2,1))
wfPgmIfEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:wfPgmIfEntry.setStatus(_A)
class _WfPgmIfCreate_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_WfPgmIfCreate_Type.__name__=_C
_WfPgmIfCreate_Object=MibTableColumn
wfPgmIfCreate=_WfPgmIfCreate_Object((1,3,6,1,4,1,18,3,5,28,2,1,1),_WfPgmIfCreate_Type())
wfPgmIfCreate.setMaxAccess(_D)
if mibBuilder.loadTexts:wfPgmIfCreate.setStatus(_A)
class _WfPgmIfEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_WfPgmIfEnable_Type.__name__=_C
_WfPgmIfEnable_Object=MibTableColumn
wfPgmIfEnable=_WfPgmIfEnable_Object((1,3,6,1,4,1,18,3,5,28,2,1,2),_WfPgmIfEnable_Type())
wfPgmIfEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:wfPgmIfEnable.setStatus(_A)
class _WfPgmIfState_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('up',1),('down',2),('init',3),(_K,4)))
_WfPgmIfState_Type.__name__=_C
_WfPgmIfState_Object=MibTableColumn
wfPgmIfState=_WfPgmIfState_Object((1,3,6,1,4,1,18,3,5,28,2,1,3),_WfPgmIfState_Type())
wfPgmIfState.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmIfState.setStatus(_A)
_WfPgmIfCct_Type=Integer32
_WfPgmIfCct_Object=MibTableColumn
wfPgmIfCct=_WfPgmIfCct_Object((1,3,6,1,4,1,18,3,5,28,2,1,4),_WfPgmIfCct_Type())
wfPgmIfCct.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmIfCct.setStatus(_A)
class _WfPgmIfNakReXmitInterval_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,2147483647))
_WfPgmIfNakReXmitInterval_Type.__name__=_C
_WfPgmIfNakReXmitInterval_Object=MibTableColumn
wfPgmIfNakReXmitInterval=_WfPgmIfNakReXmitInterval_Object((1,3,6,1,4,1,18,3,5,28,2,1,5),_WfPgmIfNakReXmitInterval_Type())
wfPgmIfNakReXmitInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:wfPgmIfNakReXmitInterval.setStatus(_A)
class _WfPgmIfMaxNakReXmitRate_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_WfPgmIfMaxNakReXmitRate_Type.__name__=_C
_WfPgmIfMaxNakReXmitRate_Object=MibTableColumn
wfPgmIfMaxNakReXmitRate=_WfPgmIfMaxNakReXmitRate_Object((1,3,6,1,4,1,18,3,5,28,2,1,6),_WfPgmIfMaxNakReXmitRate_Type())
wfPgmIfMaxNakReXmitRate.setMaxAccess(_D)
if mibBuilder.loadTexts:wfPgmIfMaxNakReXmitRate.setStatus(_A)
class _WfPgmIfNakRdataInterval_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_WfPgmIfNakRdataInterval_Type.__name__=_C
_WfPgmIfNakRdataInterval_Object=MibTableColumn
wfPgmIfNakRdataInterval=_WfPgmIfNakRdataInterval_Object((1,3,6,1,4,1,18,3,5,28,2,1,7),_WfPgmIfNakRdataInterval_Type())
wfPgmIfNakRdataInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:wfPgmIfNakRdataInterval.setStatus(_A)
class _WfPgmIfNakEliminateInterval_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_WfPgmIfNakEliminateInterval_Type.__name__=_C
_WfPgmIfNakEliminateInterval_Object=MibTableColumn
wfPgmIfNakEliminateInterval=_WfPgmIfNakEliminateInterval_Object((1,3,6,1,4,1,18,3,5,28,2,1,8),_WfPgmIfNakEliminateInterval_Type())
wfPgmIfNakEliminateInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:wfPgmIfNakEliminateInterval.setStatus(_A)
_WfPgmIfTotalReXmitStates_Type=Counter32
_WfPgmIfTotalReXmitStates_Object=MibTableColumn
wfPgmIfTotalReXmitStates=_WfPgmIfTotalReXmitStates_Object((1,3,6,1,4,1,18,3,5,28,2,1,9),_WfPgmIfTotalReXmitStates_Type())
wfPgmIfTotalReXmitStates.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmIfTotalReXmitStates.setStatus(_A)
_WfPgmIfTotalReXmitTimedOut_Type=Counter32
_WfPgmIfTotalReXmitTimedOut_Object=MibTableColumn
wfPgmIfTotalReXmitTimedOut=_WfPgmIfTotalReXmitTimedOut_Object((1,3,6,1,4,1,18,3,5,28,2,1,10),_WfPgmIfTotalReXmitTimedOut_Type())
wfPgmIfTotalReXmitTimedOut.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmIfTotalReXmitTimedOut.setStatus(_A)
_WfPgmIfInSpms_Type=Counter32
_WfPgmIfInSpms_Object=MibTableColumn
wfPgmIfInSpms=_WfPgmIfInSpms_Object((1,3,6,1,4,1,18,3,5,28,2,1,11),_WfPgmIfInSpms_Type())
wfPgmIfInSpms.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmIfInSpms.setStatus(_A)
_WfPgmIfOutSpms_Type=Counter32
_WfPgmIfOutSpms_Object=MibTableColumn
wfPgmIfOutSpms=_WfPgmIfOutSpms_Object((1,3,6,1,4,1,18,3,5,28,2,1,12),_WfPgmIfOutSpms_Type())
wfPgmIfOutSpms.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmIfOutSpms.setStatus(_A)
_WfPgmIfInParitySpms_Type=Counter32
_WfPgmIfInParitySpms_Object=MibTableColumn
wfPgmIfInParitySpms=_WfPgmIfInParitySpms_Object((1,3,6,1,4,1,18,3,5,28,2,1,13),_WfPgmIfInParitySpms_Type())
wfPgmIfInParitySpms.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmIfInParitySpms.setStatus(_A)
_WfPgmIfOutParitySpms_Type=Counter32
_WfPgmIfOutParitySpms_Object=MibTableColumn
wfPgmIfOutParitySpms=_WfPgmIfOutParitySpms_Object((1,3,6,1,4,1,18,3,5,28,2,1,14),_WfPgmIfOutParitySpms_Type())
wfPgmIfOutParitySpms.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmIfOutParitySpms.setStatus(_A)
_WfPgmIfInSpmPortErrors_Type=Counter32
_WfPgmIfInSpmPortErrors_Object=MibTableColumn
wfPgmIfInSpmPortErrors=_WfPgmIfInSpmPortErrors_Object((1,3,6,1,4,1,18,3,5,28,2,1,15),_WfPgmIfInSpmPortErrors_Type())
wfPgmIfInSpmPortErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmIfInSpmPortErrors.setStatus(_A)
_WfPgmIfInRdata_Type=Counter32
_WfPgmIfInRdata_Object=MibTableColumn
wfPgmIfInRdata=_WfPgmIfInRdata_Object((1,3,6,1,4,1,18,3,5,28,2,1,16),_WfPgmIfInRdata_Type())
wfPgmIfInRdata.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmIfInRdata.setStatus(_A)
_WfPgmIfOutRdata_Type=Counter32
_WfPgmIfOutRdata_Object=MibTableColumn
wfPgmIfOutRdata=_WfPgmIfOutRdata_Object((1,3,6,1,4,1,18,3,5,28,2,1,17),_WfPgmIfOutRdata_Type())
wfPgmIfOutRdata.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmIfOutRdata.setStatus(_A)
_WfPgmIfInParityRdata_Type=Counter32
_WfPgmIfInParityRdata_Object=MibTableColumn
wfPgmIfInParityRdata=_WfPgmIfInParityRdata_Object((1,3,6,1,4,1,18,3,5,28,2,1,18),_WfPgmIfInParityRdata_Type())
wfPgmIfInParityRdata.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmIfInParityRdata.setStatus(_A)
_WfPgmIfOutParityRdata_Type=Counter32
_WfPgmIfOutParityRdata_Object=MibTableColumn
wfPgmIfOutParityRdata=_WfPgmIfOutParityRdata_Object((1,3,6,1,4,1,18,3,5,28,2,1,19),_WfPgmIfOutParityRdata_Type())
wfPgmIfOutParityRdata.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmIfOutParityRdata.setStatus(_A)
_WfPgmIfInRdataPortErrors_Type=Counter32
_WfPgmIfInRdataPortErrors_Object=MibTableColumn
wfPgmIfInRdataPortErrors=_WfPgmIfInRdataPortErrors_Object((1,3,6,1,4,1,18,3,5,28,2,1,20),_WfPgmIfInRdataPortErrors_Type())
wfPgmIfInRdataPortErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmIfInRdataPortErrors.setStatus(_A)
_WfPgmIfInRdataNoSessionErrors_Type=Counter32
_WfPgmIfInRdataNoSessionErrors_Object=MibTableColumn
wfPgmIfInRdataNoSessionErrors=_WfPgmIfInRdataNoSessionErrors_Object((1,3,6,1,4,1,18,3,5,28,2,1,21),_WfPgmIfInRdataNoSessionErrors_Type())
wfPgmIfInRdataNoSessionErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmIfInRdataNoSessionErrors.setStatus(_A)
_WfPgmIfUniqueNaks_Type=Counter32
_WfPgmIfUniqueNaks_Object=MibTableColumn
wfPgmIfUniqueNaks=_WfPgmIfUniqueNaks_Object((1,3,6,1,4,1,18,3,5,28,2,1,22),_WfPgmIfUniqueNaks_Type())
wfPgmIfUniqueNaks.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmIfUniqueNaks.setStatus(_A)
_WfPgmIfInNaks_Type=Counter32
_WfPgmIfInNaks_Object=MibTableColumn
wfPgmIfInNaks=_WfPgmIfInNaks_Object((1,3,6,1,4,1,18,3,5,28,2,1,23),_WfPgmIfInNaks_Type())
wfPgmIfInNaks.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmIfInNaks.setStatus(_A)
_WfPgmIfOutNaks_Type=Counter32
_WfPgmIfOutNaks_Object=MibTableColumn
wfPgmIfOutNaks=_WfPgmIfOutNaks_Object((1,3,6,1,4,1,18,3,5,28,2,1,24),_WfPgmIfOutNaks_Type())
wfPgmIfOutNaks.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmIfOutNaks.setStatus(_A)
_WfPgmIfUniqueParityNaks_Type=Counter32
_WfPgmIfUniqueParityNaks_Object=MibTableColumn
wfPgmIfUniqueParityNaks=_WfPgmIfUniqueParityNaks_Object((1,3,6,1,4,1,18,3,5,28,2,1,25),_WfPgmIfUniqueParityNaks_Type())
wfPgmIfUniqueParityNaks.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmIfUniqueParityNaks.setStatus(_A)
_WfPgmIfInParityNaks_Type=Counter32
_WfPgmIfInParityNaks_Object=MibTableColumn
wfPgmIfInParityNaks=_WfPgmIfInParityNaks_Object((1,3,6,1,4,1,18,3,5,28,2,1,26),_WfPgmIfInParityNaks_Type())
wfPgmIfInParityNaks.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmIfInParityNaks.setStatus(_A)
_WfPgmIfOutParityNaks_Type=Counter32
_WfPgmIfOutParityNaks_Object=MibTableColumn
wfPgmIfOutParityNaks=_WfPgmIfOutParityNaks_Object((1,3,6,1,4,1,18,3,5,28,2,1,27),_WfPgmIfOutParityNaks_Type())
wfPgmIfOutParityNaks.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmIfOutParityNaks.setStatus(_A)
_WfPgmIfInNakPortErrors_Type=Counter32
_WfPgmIfInNakPortErrors_Object=MibTableColumn
wfPgmIfInNakPortErrors=_WfPgmIfInNakPortErrors_Object((1,3,6,1,4,1,18,3,5,28,2,1,28),_WfPgmIfInNakPortErrors_Type())
wfPgmIfInNakPortErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmIfInNakPortErrors.setStatus(_A)
_WfPgmIfInNakNoSessionErrors_Type=Counter32
_WfPgmIfInNakNoSessionErrors_Object=MibTableColumn
wfPgmIfInNakNoSessionErrors=_WfPgmIfInNakNoSessionErrors_Object((1,3,6,1,4,1,18,3,5,28,2,1,29),_WfPgmIfInNakNoSessionErrors_Type())
wfPgmIfInNakNoSessionErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmIfInNakNoSessionErrors.setStatus(_A)
_WfPgmIfInNakSeqErrors_Type=Counter32
_WfPgmIfInNakSeqErrors_Object=MibTableColumn
wfPgmIfInNakSeqErrors=_WfPgmIfInNakSeqErrors_Object((1,3,6,1,4,1,18,3,5,28,2,1,30),_WfPgmIfInNakSeqErrors_Type())
wfPgmIfInNakSeqErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmIfInNakSeqErrors.setStatus(_A)
_WfPgmIfInParityNakTgErrors_Type=Counter32
_WfPgmIfInParityNakTgErrors_Object=MibTableColumn
wfPgmIfInParityNakTgErrors=_WfPgmIfInParityNakTgErrors_Object((1,3,6,1,4,1,18,3,5,28,2,1,31),_WfPgmIfInParityNakTgErrors_Type())
wfPgmIfInParityNakTgErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmIfInParityNakTgErrors.setStatus(_A)
_WfPgmIfInNnaks_Type=Counter32
_WfPgmIfInNnaks_Object=MibTableColumn
wfPgmIfInNnaks=_WfPgmIfInNnaks_Object((1,3,6,1,4,1,18,3,5,28,2,1,32),_WfPgmIfInNnaks_Type())
wfPgmIfInNnaks.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmIfInNnaks.setStatus(_A)
_WfPgmIfOutNnaks_Type=Counter32
_WfPgmIfOutNnaks_Object=MibTableColumn
wfPgmIfOutNnaks=_WfPgmIfOutNnaks_Object((1,3,6,1,4,1,18,3,5,28,2,1,33),_WfPgmIfOutNnaks_Type())
wfPgmIfOutNnaks.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmIfOutNnaks.setStatus(_A)
_WfPgmIfInParityNnaks_Type=Counter32
_WfPgmIfInParityNnaks_Object=MibTableColumn
wfPgmIfInParityNnaks=_WfPgmIfInParityNnaks_Object((1,3,6,1,4,1,18,3,5,28,2,1,34),_WfPgmIfInParityNnaks_Type())
wfPgmIfInParityNnaks.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmIfInParityNnaks.setStatus(_A)
_WfPgmIfOutParityNnaks_Type=Counter32
_WfPgmIfOutParityNnaks_Object=MibTableColumn
wfPgmIfOutParityNnaks=_WfPgmIfOutParityNnaks_Object((1,3,6,1,4,1,18,3,5,28,2,1,35),_WfPgmIfOutParityNnaks_Type())
wfPgmIfOutParityNnaks.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmIfOutParityNnaks.setStatus(_A)
_WfPgmIfInNnakPortErrors_Type=Counter32
_WfPgmIfInNnakPortErrors_Object=MibTableColumn
wfPgmIfInNnakPortErrors=_WfPgmIfInNnakPortErrors_Object((1,3,6,1,4,1,18,3,5,28,2,1,36),_WfPgmIfInNnakPortErrors_Type())
wfPgmIfInNnakPortErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmIfInNnakPortErrors.setStatus(_A)
_WfPgmIfInNnakNoSessionErrors_Type=Counter32
_WfPgmIfInNnakNoSessionErrors_Object=MibTableColumn
wfPgmIfInNnakNoSessionErrors=_WfPgmIfInNnakNoSessionErrors_Object((1,3,6,1,4,1,18,3,5,28,2,1,37),_WfPgmIfInNnakNoSessionErrors_Type())
wfPgmIfInNnakNoSessionErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmIfInNnakNoSessionErrors.setStatus(_A)
_WfPgmIfInNcfs_Type=Counter32
_WfPgmIfInNcfs_Object=MibTableColumn
wfPgmIfInNcfs=_WfPgmIfInNcfs_Object((1,3,6,1,4,1,18,3,5,28,2,1,38),_WfPgmIfInNcfs_Type())
wfPgmIfInNcfs.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmIfInNcfs.setStatus(_A)
_WfPgmIfOutNcfs_Type=Counter32
_WfPgmIfOutNcfs_Object=MibTableColumn
wfPgmIfOutNcfs=_WfPgmIfOutNcfs_Object((1,3,6,1,4,1,18,3,5,28,2,1,39),_WfPgmIfOutNcfs_Type())
wfPgmIfOutNcfs.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmIfOutNcfs.setStatus(_A)
_WfPgmIfInParityNcfs_Type=Counter32
_WfPgmIfInParityNcfs_Object=MibTableColumn
wfPgmIfInParityNcfs=_WfPgmIfInParityNcfs_Object((1,3,6,1,4,1,18,3,5,28,2,1,40),_WfPgmIfInParityNcfs_Type())
wfPgmIfInParityNcfs.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmIfInParityNcfs.setStatus(_A)
_WfPgmIfOutParityNcfs_Type=Counter32
_WfPgmIfOutParityNcfs_Object=MibTableColumn
wfPgmIfOutParityNcfs=_WfPgmIfOutParityNcfs_Object((1,3,6,1,4,1,18,3,5,28,2,1,41),_WfPgmIfOutParityNcfs_Type())
wfPgmIfOutParityNcfs.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmIfOutParityNcfs.setStatus(_A)
_WfPgmIfInNcfPortErrors_Type=Counter32
_WfPgmIfInNcfPortErrors_Object=MibTableColumn
wfPgmIfInNcfPortErrors=_WfPgmIfInNcfPortErrors_Object((1,3,6,1,4,1,18,3,5,28,2,1,42),_WfPgmIfInNcfPortErrors_Type())
wfPgmIfInNcfPortErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmIfInNcfPortErrors.setStatus(_A)
_WfPgmIfInNcfNoSessionErrors_Type=Counter32
_WfPgmIfInNcfNoSessionErrors_Object=MibTableColumn
wfPgmIfInNcfNoSessionErrors=_WfPgmIfInNcfNoSessionErrors_Object((1,3,6,1,4,1,18,3,5,28,2,1,43),_WfPgmIfInNcfNoSessionErrors_Type())
wfPgmIfInNcfNoSessionErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmIfInNcfNoSessionErrors.setStatus(_A)
_WfPgmIfInRedirectNcfs_Type=Counter32
_WfPgmIfInRedirectNcfs_Object=MibTableColumn
wfPgmIfInRedirectNcfs=_WfPgmIfInRedirectNcfs_Object((1,3,6,1,4,1,18,3,5,28,2,1,44),_WfPgmIfInRedirectNcfs_Type())
wfPgmIfInRedirectNcfs.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmIfInRedirectNcfs.setStatus(_A)
_WfPgmSessionTable_Object=MibTable
wfPgmSessionTable=_WfPgmSessionTable_Object((1,3,6,1,4,1,18,3,5,28,3))
if mibBuilder.loadTexts:wfPgmSessionTable.setStatus(_A)
_WfPgmSessionEntry_Object=MibTableRow
wfPgmSessionEntry=_WfPgmSessionEntry_Object((1,3,6,1,4,1,18,3,5,28,3,1))
wfPgmSessionEntry.setIndexNames((0,_E,_M),(0,_E,_N),(0,_E,_O),(0,_E,_P))
if mibBuilder.loadTexts:wfPgmSessionEntry.setStatus(_A)
_WfPgmSessionSource_Type=IpAddress
_WfPgmSessionSource_Object=MibTableColumn
wfPgmSessionSource=_WfPgmSessionSource_Object((1,3,6,1,4,1,18,3,5,28,3,1,1),_WfPgmSessionSource_Type())
wfPgmSessionSource.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmSessionSource.setStatus(_A)
_WfPgmSessionGroup_Type=IpAddress
_WfPgmSessionGroup_Object=MibTableColumn
wfPgmSessionGroup=_WfPgmSessionGroup_Object((1,3,6,1,4,1,18,3,5,28,3,1,2),_WfPgmSessionGroup_Type())
wfPgmSessionGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmSessionGroup.setStatus(_A)
_WfPgmSessionSourcePort_Type=Integer32
_WfPgmSessionSourcePort_Object=MibTableColumn
wfPgmSessionSourcePort=_WfPgmSessionSourcePort_Object((1,3,6,1,4,1,18,3,5,28,3,1,3),_WfPgmSessionSourcePort_Type())
wfPgmSessionSourcePort.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmSessionSourcePort.setStatus(_A)
class _WfPgmSessionGlobalId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_WfPgmSessionGlobalId_Type.__name__=_F
_WfPgmSessionGlobalId_Object=MibTableColumn
wfPgmSessionGlobalId=_WfPgmSessionGlobalId_Object((1,3,6,1,4,1,18,3,5,28,3,1,4),_WfPgmSessionGlobalId_Type())
wfPgmSessionGlobalId.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmSessionGlobalId.setStatus(_A)
_WfPgmSessionUpstreamAddress_Type=IpAddress
_WfPgmSessionUpstreamAddress_Object=MibTableColumn
wfPgmSessionUpstreamAddress=_WfPgmSessionUpstreamAddress_Object((1,3,6,1,4,1,18,3,5,28,3,1,5),_WfPgmSessionUpstreamAddress_Type())
wfPgmSessionUpstreamAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmSessionUpstreamAddress.setStatus(_A)
_WfPgmSessionUpstreamIfCct_Type=Integer32
_WfPgmSessionUpstreamIfCct_Object=MibTableColumn
wfPgmSessionUpstreamIfCct=_WfPgmSessionUpstreamIfCct_Object((1,3,6,1,4,1,18,3,5,28,3,1,6),_WfPgmSessionUpstreamIfCct_Type())
wfPgmSessionUpstreamIfCct.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmSessionUpstreamIfCct.setStatus(_A)
_WfPgmSessionTrailEdgeSeq_Type=Counter32
_WfPgmSessionTrailEdgeSeq_Object=MibTableColumn
wfPgmSessionTrailEdgeSeq=_WfPgmSessionTrailEdgeSeq_Object((1,3,6,1,4,1,18,3,5,28,3,1,7),_WfPgmSessionTrailEdgeSeq_Type())
wfPgmSessionTrailEdgeSeq.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmSessionTrailEdgeSeq.setStatus(_A)
_WfPgmSessionIncrSeq_Type=Counter32
_WfPgmSessionIncrSeq_Object=MibTableColumn
wfPgmSessionIncrSeq=_WfPgmSessionIncrSeq_Object((1,3,6,1,4,1,18,3,5,28,3,1,8),_WfPgmSessionIncrSeq_Type())
wfPgmSessionIncrSeq.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmSessionIncrSeq.setStatus(_A)
_WfPgmSessionLeadEdgeSeq_Type=Counter32
_WfPgmSessionLeadEdgeSeq_Object=MibTableColumn
wfPgmSessionLeadEdgeSeq=_WfPgmSessionLeadEdgeSeq_Object((1,3,6,1,4,1,18,3,5,28,3,1,9),_WfPgmSessionLeadEdgeSeq_Type())
wfPgmSessionLeadEdgeSeq.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmSessionLeadEdgeSeq.setStatus(_A)
_WfPgmSessionInSpms_Type=Counter32
_WfPgmSessionInSpms_Object=MibTableColumn
wfPgmSessionInSpms=_WfPgmSessionInSpms_Object((1,3,6,1,4,1,18,3,5,28,3,1,10),_WfPgmSessionInSpms_Type())
wfPgmSessionInSpms.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmSessionInSpms.setStatus(_A)
_WfPgmSessionOutSpms_Type=Counter32
_WfPgmSessionOutSpms_Object=MibTableColumn
wfPgmSessionOutSpms=_WfPgmSessionOutSpms_Object((1,3,6,1,4,1,18,3,5,28,3,1,11),_WfPgmSessionOutSpms_Type())
wfPgmSessionOutSpms.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmSessionOutSpms.setStatus(_A)
_WfPgmSessionInParitySpms_Type=Counter32
_WfPgmSessionInParitySpms_Object=MibTableColumn
wfPgmSessionInParitySpms=_WfPgmSessionInParitySpms_Object((1,3,6,1,4,1,18,3,5,28,3,1,12),_WfPgmSessionInParitySpms_Type())
wfPgmSessionInParitySpms.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmSessionInParitySpms.setStatus(_A)
_WfPgmSessionOutParitySpms_Type=Counter32
_WfPgmSessionOutParitySpms_Object=MibTableColumn
wfPgmSessionOutParitySpms=_WfPgmSessionOutParitySpms_Object((1,3,6,1,4,1,18,3,5,28,3,1,13),_WfPgmSessionOutParitySpms_Type())
wfPgmSessionOutParitySpms.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmSessionOutParitySpms.setStatus(_A)
_WfPgmSessionTotalReXmitStates_Type=Counter32
_WfPgmSessionTotalReXmitStates_Object=MibTableColumn
wfPgmSessionTotalReXmitStates=_WfPgmSessionTotalReXmitStates_Object((1,3,6,1,4,1,18,3,5,28,3,1,14),_WfPgmSessionTotalReXmitStates_Type())
wfPgmSessionTotalReXmitStates.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmSessionTotalReXmitStates.setStatus(_A)
_WfPgmSessionTotalReXmitTimedOut_Type=Counter32
_WfPgmSessionTotalReXmitTimedOut_Object=MibTableColumn
wfPgmSessionTotalReXmitTimedOut=_WfPgmSessionTotalReXmitTimedOut_Object((1,3,6,1,4,1,18,3,5,28,3,1,15),_WfPgmSessionTotalReXmitTimedOut_Type())
wfPgmSessionTotalReXmitTimedOut.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmSessionTotalReXmitTimedOut.setStatus(_A)
_WfPgmSessionInRdata_Type=Counter32
_WfPgmSessionInRdata_Object=MibTableColumn
wfPgmSessionInRdata=_WfPgmSessionInRdata_Object((1,3,6,1,4,1,18,3,5,28,3,1,16),_WfPgmSessionInRdata_Type())
wfPgmSessionInRdata.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmSessionInRdata.setStatus(_A)
_WfPgmSessionOutRdata_Type=Counter32
_WfPgmSessionOutRdata_Object=MibTableColumn
wfPgmSessionOutRdata=_WfPgmSessionOutRdata_Object((1,3,6,1,4,1,18,3,5,28,3,1,17),_WfPgmSessionOutRdata_Type())
wfPgmSessionOutRdata.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmSessionOutRdata.setStatus(_A)
_WfPgmSessionInParityRdata_Type=Counter32
_WfPgmSessionInParityRdata_Object=MibTableColumn
wfPgmSessionInParityRdata=_WfPgmSessionInParityRdata_Object((1,3,6,1,4,1,18,3,5,28,3,1,18),_WfPgmSessionInParityRdata_Type())
wfPgmSessionInParityRdata.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmSessionInParityRdata.setStatus(_A)
_WfPgmSessionOutParityRdata_Type=Counter32
_WfPgmSessionOutParityRdata_Object=MibTableColumn
wfPgmSessionOutParityRdata=_WfPgmSessionOutParityRdata_Object((1,3,6,1,4,1,18,3,5,28,3,1,19),_WfPgmSessionOutParityRdata_Type())
wfPgmSessionOutParityRdata.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmSessionOutParityRdata.setStatus(_A)
_WfPgmSessionInRdataNoStateErrors_Type=Counter32
_WfPgmSessionInRdataNoStateErrors_Object=MibTableColumn
wfPgmSessionInRdataNoStateErrors=_WfPgmSessionInRdataNoStateErrors_Object((1,3,6,1,4,1,18,3,5,28,3,1,20),_WfPgmSessionInRdataNoStateErrors_Type())
wfPgmSessionInRdataNoStateErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmSessionInRdataNoStateErrors.setStatus(_A)
_WfPgmSessionUniqueNaks_Type=Counter32
_WfPgmSessionUniqueNaks_Object=MibTableColumn
wfPgmSessionUniqueNaks=_WfPgmSessionUniqueNaks_Object((1,3,6,1,4,1,18,3,5,28,3,1,21),_WfPgmSessionUniqueNaks_Type())
wfPgmSessionUniqueNaks.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmSessionUniqueNaks.setStatus(_A)
_WfPgmSessionInNaks_Type=Counter32
_WfPgmSessionInNaks_Object=MibTableColumn
wfPgmSessionInNaks=_WfPgmSessionInNaks_Object((1,3,6,1,4,1,18,3,5,28,3,1,22),_WfPgmSessionInNaks_Type())
wfPgmSessionInNaks.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmSessionInNaks.setStatus(_A)
_WfPgmSessionOutNaks_Type=Counter32
_WfPgmSessionOutNaks_Object=MibTableColumn
wfPgmSessionOutNaks=_WfPgmSessionOutNaks_Object((1,3,6,1,4,1,18,3,5,28,3,1,23),_WfPgmSessionOutNaks_Type())
wfPgmSessionOutNaks.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmSessionOutNaks.setStatus(_A)
_WfPgmSessionUniqueParityNaks_Type=Counter32
_WfPgmSessionUniqueParityNaks_Object=MibTableColumn
wfPgmSessionUniqueParityNaks=_WfPgmSessionUniqueParityNaks_Object((1,3,6,1,4,1,18,3,5,28,3,1,24),_WfPgmSessionUniqueParityNaks_Type())
wfPgmSessionUniqueParityNaks.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmSessionUniqueParityNaks.setStatus(_A)
_WfPgmSessionInParityNaks_Type=Counter32
_WfPgmSessionInParityNaks_Object=MibTableColumn
wfPgmSessionInParityNaks=_WfPgmSessionInParityNaks_Object((1,3,6,1,4,1,18,3,5,28,3,1,25),_WfPgmSessionInParityNaks_Type())
wfPgmSessionInParityNaks.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmSessionInParityNaks.setStatus(_A)
_WfPgmSessionOutParityNaks_Type=Counter32
_WfPgmSessionOutParityNaks_Object=MibTableColumn
wfPgmSessionOutParityNaks=_WfPgmSessionOutParityNaks_Object((1,3,6,1,4,1,18,3,5,28,3,1,26),_WfPgmSessionOutParityNaks_Type())
wfPgmSessionOutParityNaks.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmSessionOutParityNaks.setStatus(_A)
_WfPgmSessionInNakSeqErrors_Type=Counter32
_WfPgmSessionInNakSeqErrors_Object=MibTableColumn
wfPgmSessionInNakSeqErrors=_WfPgmSessionInNakSeqErrors_Object((1,3,6,1,4,1,18,3,5,28,3,1,27),_WfPgmSessionInNakSeqErrors_Type())
wfPgmSessionInNakSeqErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmSessionInNakSeqErrors.setStatus(_A)
_WfPgmSessionInNnaks_Type=Counter32
_WfPgmSessionInNnaks_Object=MibTableColumn
wfPgmSessionInNnaks=_WfPgmSessionInNnaks_Object((1,3,6,1,4,1,18,3,5,28,3,1,28),_WfPgmSessionInNnaks_Type())
wfPgmSessionInNnaks.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmSessionInNnaks.setStatus(_A)
_WfPgmSessionOutNnaks_Type=Counter32
_WfPgmSessionOutNnaks_Object=MibTableColumn
wfPgmSessionOutNnaks=_WfPgmSessionOutNnaks_Object((1,3,6,1,4,1,18,3,5,28,3,1,29),_WfPgmSessionOutNnaks_Type())
wfPgmSessionOutNnaks.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmSessionOutNnaks.setStatus(_A)
_WfPgmSessionInParityNnaks_Type=Counter32
_WfPgmSessionInParityNnaks_Object=MibTableColumn
wfPgmSessionInParityNnaks=_WfPgmSessionInParityNnaks_Object((1,3,6,1,4,1,18,3,5,28,3,1,30),_WfPgmSessionInParityNnaks_Type())
wfPgmSessionInParityNnaks.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmSessionInParityNnaks.setStatus(_A)
_WfPgmSessionOutParityNnaks_Type=Counter32
_WfPgmSessionOutParityNnaks_Object=MibTableColumn
wfPgmSessionOutParityNnaks=_WfPgmSessionOutParityNnaks_Object((1,3,6,1,4,1,18,3,5,28,3,1,31),_WfPgmSessionOutParityNnaks_Type())
wfPgmSessionOutParityNnaks.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmSessionOutParityNnaks.setStatus(_A)
_WfPgmSessionInNcfs_Type=Counter32
_WfPgmSessionInNcfs_Object=MibTableColumn
wfPgmSessionInNcfs=_WfPgmSessionInNcfs_Object((1,3,6,1,4,1,18,3,5,28,3,1,32),_WfPgmSessionInNcfs_Type())
wfPgmSessionInNcfs.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmSessionInNcfs.setStatus(_A)
_WfPgmSessionOutNcfs_Type=Counter32
_WfPgmSessionOutNcfs_Object=MibTableColumn
wfPgmSessionOutNcfs=_WfPgmSessionOutNcfs_Object((1,3,6,1,4,1,18,3,5,28,3,1,33),_WfPgmSessionOutNcfs_Type())
wfPgmSessionOutNcfs.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmSessionOutNcfs.setStatus(_A)
_WfPgmSessionInParityNcfs_Type=Counter32
_WfPgmSessionInParityNcfs_Object=MibTableColumn
wfPgmSessionInParityNcfs=_WfPgmSessionInParityNcfs_Object((1,3,6,1,4,1,18,3,5,28,3,1,34),_WfPgmSessionInParityNcfs_Type())
wfPgmSessionInParityNcfs.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmSessionInParityNcfs.setStatus(_A)
_WfPgmSessionOutParityNcfs_Type=Counter32
_WfPgmSessionOutParityNcfs_Object=MibTableColumn
wfPgmSessionOutParityNcfs=_WfPgmSessionOutParityNcfs_Object((1,3,6,1,4,1,18,3,5,28,3,1,35),_WfPgmSessionOutParityNcfs_Type())
wfPgmSessionOutParityNcfs.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmSessionOutParityNcfs.setStatus(_A)
_WfPgmSessionInRedirectNcfs_Type=Counter32
_WfPgmSessionInRedirectNcfs_Object=MibTableColumn
wfPgmSessionInRedirectNcfs=_WfPgmSessionInRedirectNcfs_Object((1,3,6,1,4,1,18,3,5,28,3,1,36),_WfPgmSessionInRedirectNcfs_Type())
wfPgmSessionInRedirectNcfs.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmSessionInRedirectNcfs.setStatus(_A)
_WfPgmReXmitTable_Object=MibTable
wfPgmReXmitTable=_WfPgmReXmitTable_Object((1,3,6,1,4,1,18,3,5,28,4))
if mibBuilder.loadTexts:wfPgmReXmitTable.setStatus(_A)
_WfPgmReXmitEntry_Object=MibTableRow
wfPgmReXmitEntry=_WfPgmReXmitEntry_Object((1,3,6,1,4,1,18,3,5,28,4,1))
wfPgmReXmitEntry.setIndexNames((0,_E,_Q),(0,_E,_R),(0,_E,_S),(0,_E,_T),(0,_E,_U),(0,_E,_V))
if mibBuilder.loadTexts:wfPgmReXmitEntry.setStatus(_A)
_WfPgmReXmitSource_Type=IpAddress
_WfPgmReXmitSource_Object=MibTableColumn
wfPgmReXmitSource=_WfPgmReXmitSource_Object((1,3,6,1,4,1,18,3,5,28,4,1,1),_WfPgmReXmitSource_Type())
wfPgmReXmitSource.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmReXmitSource.setStatus(_A)
_WfPgmReXmitGroup_Type=IpAddress
_WfPgmReXmitGroup_Object=MibTableColumn
wfPgmReXmitGroup=_WfPgmReXmitGroup_Object((1,3,6,1,4,1,18,3,5,28,4,1,2),_WfPgmReXmitGroup_Type())
wfPgmReXmitGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmReXmitGroup.setStatus(_A)
_WfPgmReXmitSourcePort_Type=Integer32
_WfPgmReXmitSourcePort_Object=MibTableColumn
wfPgmReXmitSourcePort=_WfPgmReXmitSourcePort_Object((1,3,6,1,4,1,18,3,5,28,4,1,3),_WfPgmReXmitSourcePort_Type())
wfPgmReXmitSourcePort.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmReXmitSourcePort.setStatus(_A)
class _WfPgmReXmitGlobalId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_WfPgmReXmitGlobalId_Type.__name__=_F
_WfPgmReXmitGlobalId_Object=MibTableColumn
wfPgmReXmitGlobalId=_WfPgmReXmitGlobalId_Object((1,3,6,1,4,1,18,3,5,28,4,1,4),_WfPgmReXmitGlobalId_Type())
wfPgmReXmitGlobalId.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmReXmitGlobalId.setStatus(_A)
_WfPgmReXmitSelectiveSeqNum_Type=Integer32
_WfPgmReXmitSelectiveSeqNum_Object=MibTableColumn
wfPgmReXmitSelectiveSeqNum=_WfPgmReXmitSelectiveSeqNum_Object((1,3,6,1,4,1,18,3,5,28,4,1,5),_WfPgmReXmitSelectiveSeqNum_Type())
wfPgmReXmitSelectiveSeqNum.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmReXmitSelectiveSeqNum.setStatus(_A)
_WfPgmReXmitParityTgSeqNum_Type=Integer32
_WfPgmReXmitParityTgSeqNum_Object=MibTableColumn
wfPgmReXmitParityTgSeqNum=_WfPgmReXmitParityTgSeqNum_Object((1,3,6,1,4,1,18,3,5,28,4,1,6),_WfPgmReXmitParityTgSeqNum_Type())
wfPgmReXmitParityTgSeqNum.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmReXmitParityTgSeqNum.setStatus(_A)
_WfPgmReXmitReqParityTgCount_Type=Integer32
_WfPgmReXmitReqParityTgCount_Object=MibTableColumn
wfPgmReXmitReqParityTgCount=_WfPgmReXmitReqParityTgCount_Object((1,3,6,1,4,1,18,3,5,28,4,1,7),_WfPgmReXmitReqParityTgCount_Type())
wfPgmReXmitReqParityTgCount.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmReXmitReqParityTgCount.setStatus(_A)
_WfPgmReXmitUpStreamCct_Type=Integer32
_WfPgmReXmitUpStreamCct_Object=MibTableColumn
wfPgmReXmitUpStreamCct=_WfPgmReXmitUpStreamCct_Object((1,3,6,1,4,1,18,3,5,28,4,1,8),_WfPgmReXmitUpStreamCct_Type())
wfPgmReXmitUpStreamCct.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmReXmitUpStreamCct.setStatus(_A)
_WfPgmReXmitDownStream_Type=OctetString
_WfPgmReXmitDownStream_Object=MibTableColumn
wfPgmReXmitDownStream=_WfPgmReXmitDownStream_Object((1,3,6,1,4,1,18,3,5,28,4,1,9),_WfPgmReXmitDownStream_Type())
wfPgmReXmitDownStream.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPgmReXmitDownStream.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'wfPgm':wfPgm,'wfPgmCreate':wfPgmCreate,'wfPgmEnable':wfPgmEnable,'wfPgmState':wfPgmState,'wfPgmDebug':wfPgmDebug,'wfPgmSessionLifeTime':wfPgmSessionLifeTime,'wfPgmNnakGenerate':wfPgmNnakGenerate,'wfPgmMaxReXmitStates':wfPgmMaxReXmitStates,'wfPgmTotalReXmitStates':wfPgmTotalReXmitStates,'wfPgmMaxSessions':wfPgmMaxSessions,'wfPgmTotalSessions':wfPgmTotalSessions,'wfPgmTotalReXmitStatesTimedOut':wfPgmTotalReXmitStatesTimedOut,'wfPgmTotalUniqueNaks':wfPgmTotalUniqueNaks,'wfPgmTotalUniqueParityNaks':wfPgmTotalUniqueParityNaks,'wfPgmMaxNakRate':wfPgmMaxNakRate,'wfPgmIfTable':wfPgmIfTable,'wfPgmIfEntry':wfPgmIfEntry,'wfPgmIfCreate':wfPgmIfCreate,'wfPgmIfEnable':wfPgmIfEnable,'wfPgmIfState':wfPgmIfState,_L:wfPgmIfCct,'wfPgmIfNakReXmitInterval':wfPgmIfNakReXmitInterval,'wfPgmIfMaxNakReXmitRate':wfPgmIfMaxNakReXmitRate,'wfPgmIfNakRdataInterval':wfPgmIfNakRdataInterval,'wfPgmIfNakEliminateInterval':wfPgmIfNakEliminateInterval,'wfPgmIfTotalReXmitStates':wfPgmIfTotalReXmitStates,'wfPgmIfTotalReXmitTimedOut':wfPgmIfTotalReXmitTimedOut,'wfPgmIfInSpms':wfPgmIfInSpms,'wfPgmIfOutSpms':wfPgmIfOutSpms,'wfPgmIfInParitySpms':wfPgmIfInParitySpms,'wfPgmIfOutParitySpms':wfPgmIfOutParitySpms,'wfPgmIfInSpmPortErrors':wfPgmIfInSpmPortErrors,'wfPgmIfInRdata':wfPgmIfInRdata,'wfPgmIfOutRdata':wfPgmIfOutRdata,'wfPgmIfInParityRdata':wfPgmIfInParityRdata,'wfPgmIfOutParityRdata':wfPgmIfOutParityRdata,'wfPgmIfInRdataPortErrors':wfPgmIfInRdataPortErrors,'wfPgmIfInRdataNoSessionErrors':wfPgmIfInRdataNoSessionErrors,'wfPgmIfUniqueNaks':wfPgmIfUniqueNaks,'wfPgmIfInNaks':wfPgmIfInNaks,'wfPgmIfOutNaks':wfPgmIfOutNaks,'wfPgmIfUniqueParityNaks':wfPgmIfUniqueParityNaks,'wfPgmIfInParityNaks':wfPgmIfInParityNaks,'wfPgmIfOutParityNaks':wfPgmIfOutParityNaks,'wfPgmIfInNakPortErrors':wfPgmIfInNakPortErrors,'wfPgmIfInNakNoSessionErrors':wfPgmIfInNakNoSessionErrors,'wfPgmIfInNakSeqErrors':wfPgmIfInNakSeqErrors,'wfPgmIfInParityNakTgErrors':wfPgmIfInParityNakTgErrors,'wfPgmIfInNnaks':wfPgmIfInNnaks,'wfPgmIfOutNnaks':wfPgmIfOutNnaks,'wfPgmIfInParityNnaks':wfPgmIfInParityNnaks,'wfPgmIfOutParityNnaks':wfPgmIfOutParityNnaks,'wfPgmIfInNnakPortErrors':wfPgmIfInNnakPortErrors,'wfPgmIfInNnakNoSessionErrors':wfPgmIfInNnakNoSessionErrors,'wfPgmIfInNcfs':wfPgmIfInNcfs,'wfPgmIfOutNcfs':wfPgmIfOutNcfs,'wfPgmIfInParityNcfs':wfPgmIfInParityNcfs,'wfPgmIfOutParityNcfs':wfPgmIfOutParityNcfs,'wfPgmIfInNcfPortErrors':wfPgmIfInNcfPortErrors,'wfPgmIfInNcfNoSessionErrors':wfPgmIfInNcfNoSessionErrors,'wfPgmIfInRedirectNcfs':wfPgmIfInRedirectNcfs,'wfPgmSessionTable':wfPgmSessionTable,'wfPgmSessionEntry':wfPgmSessionEntry,_M:wfPgmSessionSource,_N:wfPgmSessionGroup,_O:wfPgmSessionSourcePort,_P:wfPgmSessionGlobalId,'wfPgmSessionUpstreamAddress':wfPgmSessionUpstreamAddress,'wfPgmSessionUpstreamIfCct':wfPgmSessionUpstreamIfCct,'wfPgmSessionTrailEdgeSeq':wfPgmSessionTrailEdgeSeq,'wfPgmSessionIncrSeq':wfPgmSessionIncrSeq,'wfPgmSessionLeadEdgeSeq':wfPgmSessionLeadEdgeSeq,'wfPgmSessionInSpms':wfPgmSessionInSpms,'wfPgmSessionOutSpms':wfPgmSessionOutSpms,'wfPgmSessionInParitySpms':wfPgmSessionInParitySpms,'wfPgmSessionOutParitySpms':wfPgmSessionOutParitySpms,'wfPgmSessionTotalReXmitStates':wfPgmSessionTotalReXmitStates,'wfPgmSessionTotalReXmitTimedOut':wfPgmSessionTotalReXmitTimedOut,'wfPgmSessionInRdata':wfPgmSessionInRdata,'wfPgmSessionOutRdata':wfPgmSessionOutRdata,'wfPgmSessionInParityRdata':wfPgmSessionInParityRdata,'wfPgmSessionOutParityRdata':wfPgmSessionOutParityRdata,'wfPgmSessionInRdataNoStateErrors':wfPgmSessionInRdataNoStateErrors,'wfPgmSessionUniqueNaks':wfPgmSessionUniqueNaks,'wfPgmSessionInNaks':wfPgmSessionInNaks,'wfPgmSessionOutNaks':wfPgmSessionOutNaks,'wfPgmSessionUniqueParityNaks':wfPgmSessionUniqueParityNaks,'wfPgmSessionInParityNaks':wfPgmSessionInParityNaks,'wfPgmSessionOutParityNaks':wfPgmSessionOutParityNaks,'wfPgmSessionInNakSeqErrors':wfPgmSessionInNakSeqErrors,'wfPgmSessionInNnaks':wfPgmSessionInNnaks,'wfPgmSessionOutNnaks':wfPgmSessionOutNnaks,'wfPgmSessionInParityNnaks':wfPgmSessionInParityNnaks,'wfPgmSessionOutParityNnaks':wfPgmSessionOutParityNnaks,'wfPgmSessionInNcfs':wfPgmSessionInNcfs,'wfPgmSessionOutNcfs':wfPgmSessionOutNcfs,'wfPgmSessionInParityNcfs':wfPgmSessionInParityNcfs,'wfPgmSessionOutParityNcfs':wfPgmSessionOutParityNcfs,'wfPgmSessionInRedirectNcfs':wfPgmSessionInRedirectNcfs,'wfPgmReXmitTable':wfPgmReXmitTable,'wfPgmReXmitEntry':wfPgmReXmitEntry,_Q:wfPgmReXmitSource,_R:wfPgmReXmitGroup,_S:wfPgmReXmitSourcePort,_T:wfPgmReXmitGlobalId,_U:wfPgmReXmitSelectiveSeqNum,_V:wfPgmReXmitParityTgSeqNum,'wfPgmReXmitReqParityTgCount':wfPgmReXmitReqParityTgCount,'wfPgmReXmitUpStreamCct':wfPgmReXmitUpStreamCct,'wfPgmReXmitDownStream':wfPgmReXmitDownStream})