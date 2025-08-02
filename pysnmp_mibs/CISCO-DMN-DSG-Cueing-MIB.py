_F='cueingToneSeqNum'
_E='CISCO-DMN-DSG-Cueing-MIB'
_D='trigger'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoDSGUtilities,=mibBuilder.importSymbols('CISCO-DMN-DSG-ROOT-MIB','ciscoDSGUtilities')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoDSGCueing=ModuleIdentity((1,3,6,1,4,1,1429,2,2,5,33))
if mibBuilder.loadTexts:ciscoDSGCueing.setRevisions(('2010-08-30 08:00',))
class _CueingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),('tone',2)))
_CueingMode_Type.__name__=_B
_CueingMode_Object=MibScalar
cueingMode=_CueingMode_Object((1,3,6,1,4,1,1429,2,2,5,33,1),_CueingMode_Type())
cueingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cueingMode.setStatus(_A)
class _CueingTrigPol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('low',1),('high',2)))
_CueingTrigPol_Type.__name__=_B
_CueingTrigPol_Object=MibScalar
cueingTrigPol=_CueingTrigPol_Object((1,3,6,1,4,1,1429,2,2,5,33,2),_CueingTrigPol_Type())
cueingTrigPol.setMaxAccess(_C)
if mibBuilder.loadTexts:cueingTrigPol.setStatus(_A)
class _CueingRepeatCnt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_CueingRepeatCnt_Type.__name__=_B
_CueingRepeatCnt_Object=MibScalar
cueingRepeatCnt=_CueingRepeatCnt_Object((1,3,6,1,4,1,1429,2,2,5,33,3),_CueingRepeatCnt_Type())
cueingRepeatCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:cueingRepeatCnt.setStatus(_A)
class _CueingTone_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,80))
_CueingTone_Type.__name__=_B
_CueingTone_Object=MibScalar
cueingTone=_CueingTone_Object((1,3,6,1,4,1,1429,2,2,5,33,4),_CueingTone_Type())
cueingTone.setMaxAccess(_C)
if mibBuilder.loadTexts:cueingTone.setStatus(_A)
class _CueingSilence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,80))
_CueingSilence_Type.__name__=_B
_CueingSilence_Object=MibScalar
cueingSilence=_CueingSilence_Object((1,3,6,1,4,1,1429,2,2,5,33,5),_CueingSilence_Type())
cueingSilence.setMaxAccess(_C)
if mibBuilder.loadTexts:cueingSilence.setStatus(_A)
class _CueingRelayMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('alarm',1),(_D,2)))
_CueingRelayMode_Type.__name__=_B
_CueingRelayMode_Object=MibScalar
cueingRelayMode=_CueingRelayMode_Object((1,3,6,1,4,1,1429,2,2,5,33,6),_CueingRelayMode_Type())
cueingRelayMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cueingRelayMode.setStatus(_A)
class _CueingRelayTrigBit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_CueingRelayTrigBit_Type.__name__=_B
_CueingRelayTrigBit_Object=MibScalar
cueingRelayTrigBit=_CueingRelayTrigBit_Object((1,3,6,1,4,1,1429,2,2,5,33,7),_CueingRelayTrigBit_Type())
cueingRelayTrigBit.setMaxAccess(_C)
if mibBuilder.loadTexts:cueingRelayTrigBit.setStatus(_A)
class _CueingTestToneSequence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999))
_CueingTestToneSequence_Type.__name__=_B
_CueingTestToneSequence_Object=MibScalar
cueingTestToneSequence=_CueingTestToneSequence_Object((1,3,6,1,4,1,1429,2,2,5,33,8),_CueingTestToneSequence_Type())
cueingTestToneSequence.setMaxAccess(_C)
if mibBuilder.loadTexts:cueingTestToneSequence.setStatus(_A)
class _CueingTestToneStartStop_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('stop',2)))
_CueingTestToneStartStop_Type.__name__=_B
_CueingTestToneStartStop_Object=MibScalar
cueingTestToneStartStop=_CueingTestToneStartStop_Object((1,3,6,1,4,1,1429,2,2,5,33,9),_CueingTestToneStartStop_Type())
cueingTestToneStartStop.setMaxAccess(_C)
if mibBuilder.loadTexts:cueingTestToneStartStop.setStatus(_A)
class _CueingTestToneGo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('no',1),('yes',2)))
_CueingTestToneGo_Type.__name__=_B
_CueingTestToneGo_Object=MibScalar
cueingTestToneGo=_CueingTestToneGo_Object((1,3,6,1,4,1,1429,2,2,5,33,10),_CueingTestToneGo_Type())
cueingTestToneGo.setMaxAccess(_C)
if mibBuilder.loadTexts:cueingTestToneGo.setStatus(_A)
_CueingTable_ObjectIdentity=ObjectIdentity
cueingTable=_CueingTable_ObjectIdentity((1,3,6,1,4,1,1429,2,2,5,33,11))
_CueingToneSeqTable_Object=MibTable
cueingToneSeqTable=_CueingToneSeqTable_Object((1,3,6,1,4,1,1429,2,2,5,33,11,1))
if mibBuilder.loadTexts:cueingToneSeqTable.setStatus(_A)
_CueingToneSeqEntry_Object=MibTableRow
cueingToneSeqEntry=_CueingToneSeqEntry_Object((1,3,6,1,4,1,1429,2,2,5,33,11,1,1))
cueingToneSeqEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:cueingToneSeqEntry.setStatus(_A)
class _CueingToneSeqNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_CueingToneSeqNum_Type.__name__=_B
_CueingToneSeqNum_Object=MibTableColumn
cueingToneSeqNum=_CueingToneSeqNum_Object((1,3,6,1,4,1,1429,2,2,5,33,11,1,1,1),_CueingToneSeqNum_Type())
cueingToneSeqNum.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cueingToneSeqNum.setStatus(_A)
class _CueingToneSeqState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disable',1),('enable',2)))
_CueingToneSeqState_Type.__name__=_B
_CueingToneSeqState_Object=MibTableColumn
cueingToneSeqState=_CueingToneSeqState_Object((1,3,6,1,4,1,1429,2,2,5,33,11,1,1,2),_CueingToneSeqState_Type())
cueingToneSeqState.setMaxAccess(_C)
if mibBuilder.loadTexts:cueingToneSeqState.setStatus(_A)
class _CueingToneSeqTones_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999))
_CueingToneSeqTones_Type.__name__=_B
_CueingToneSeqTones_Object=MibTableColumn
cueingToneSeqTones=_CueingToneSeqTones_Object((1,3,6,1,4,1,1429,2,2,5,33,11,1,1,3),_CueingToneSeqTones_Type())
cueingToneSeqTones.setMaxAccess(_C)
if mibBuilder.loadTexts:cueingToneSeqTones.setStatus(_A)
class _CueingToneSeqMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('start',1),('stop',2),('both',3)))
_CueingToneSeqMode_Type.__name__=_B
_CueingToneSeqMode_Object=MibTableColumn
cueingToneSeqMode=_CueingToneSeqMode_Object((1,3,6,1,4,1,1429,2,2,5,33,11,1,1,4),_CueingToneSeqMode_Type())
cueingToneSeqMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cueingToneSeqMode.setStatus(_A)
class _CueingToneSeqDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_CueingToneSeqDelay_Type.__name__=_B
_CueingToneSeqDelay_Object=MibTableColumn
cueingToneSeqDelay=_CueingToneSeqDelay_Object((1,3,6,1,4,1,1429,2,2,5,33,11,1,1,5),_CueingToneSeqDelay_Type())
cueingToneSeqDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:cueingToneSeqDelay.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'ciscoDSGCueing':ciscoDSGCueing,'cueingMode':cueingMode,'cueingTrigPol':cueingTrigPol,'cueingRepeatCnt':cueingRepeatCnt,'cueingTone':cueingTone,'cueingSilence':cueingSilence,'cueingRelayMode':cueingRelayMode,'cueingRelayTrigBit':cueingRelayTrigBit,'cueingTestToneSequence':cueingTestToneSequence,'cueingTestToneStartStop':cueingTestToneStartStop,'cueingTestToneGo':cueingTestToneGo,'cueingTable':cueingTable,'cueingToneSeqTable':cueingToneSeqTable,'cueingToneSeqEntry':cueingToneSeqEntry,_F:cueingToneSeqNum,'cueingToneSeqState':cueingToneSeqState,'cueingToneSeqTones':cueingToneSeqTones,'cueingToneSeqMode':cueingToneSeqMode,'cueingToneSeqDelay':cueingToneSeqDelay})