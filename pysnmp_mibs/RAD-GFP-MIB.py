_Q='enable'
_P='disable'
_O='gfpCnfgIdx'
_N='RAD-GFP-MIB'
_M='ifIndex'
_L='read-write'
_K='alarmEventReason'
_J='alarmEventLogSourceName'
_I='alarmEventLogSeverity'
_H='alarmEventLogDescription'
_G='alarmEventLogDateAndTime'
_F='alarmEventLogAlarmOrEventId'
_E='ifAlias'
_D='Integer32'
_C='IF-MIB'
_B='current'
_A='RAD-GEN-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifAlias,ifIndex=mibBuilder.importSymbols(_C,_E,_M)
alarmEventLogAlarmOrEventId,alarmEventLogDateAndTime,alarmEventLogDescription,alarmEventLogSeverity,alarmEventLogSourceName,alarmEventReason=mibBuilder.importSymbols(_A,_F,_G,_H,_I,_J,_K)
agnt,=mibBuilder.importSymbols('RAD-SMI-MIB','agnt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
gfp=ModuleIdentity((1,3,6,1,4,1,164,6,2,55))
_GfpEvents_ObjectIdentity=ObjectIdentity
gfpEvents=_GfpEvents_ObjectIdentity((1,3,6,1,4,1,164,6,2,55,0))
_GfpCnfgTable_Object=MibTable
gfpCnfgTable=_GfpCnfgTable_Object((1,3,6,1,4,1,164,6,2,55,1))
if mibBuilder.loadTexts:gfpCnfgTable.setStatus(_B)
_GfpCnfgEntry_Object=MibTableRow
gfpCnfgEntry=_GfpCnfgEntry_Object((1,3,6,1,4,1,164,6,2,55,1,1))
gfpCnfgEntry.setIndexNames((0,_C,_M),(0,_N,_O))
if mibBuilder.loadTexts:gfpCnfgEntry.setStatus(_B)
_GfpCnfgIdx_Type=Unsigned32
_GfpCnfgIdx_Object=MibTableColumn
gfpCnfgIdx=_GfpCnfgIdx_Object((1,3,6,1,4,1,164,6,2,55,1,1,1),_GfpCnfgIdx_Type())
gfpCnfgIdx.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:gfpCnfgIdx.setStatus(_B)
class _GfpPayloadFcs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_P,2),(_Q,3)))
_GfpPayloadFcs_Type.__name__=_D
_GfpPayloadFcs_Object=MibTableColumn
gfpPayloadFcs=_GfpPayloadFcs_Object((1,3,6,1,4,1,164,6,2,55,1,1,2),_GfpPayloadFcs_Type())
gfpPayloadFcs.setMaxAccess(_L)
if mibBuilder.loadTexts:gfpPayloadFcs.setStatus(_B)
class _GfpRxTxScramble_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noScramble',1),('rxTxScramble',2),('rxOnlyScramble',3),('txOnlyScramble',4)))
_GfpRxTxScramble_Type.__name__=_D
_GfpRxTxScramble_Object=MibTableColumn
gfpRxTxScramble=_GfpRxTxScramble_Object((1,3,6,1,4,1,164,6,2,55,1,1,3),_GfpRxTxScramble_Type())
gfpRxTxScramble.setMaxAccess(_L)
if mibBuilder.loadTexts:gfpRxTxScramble.setStatus(_B)
class _GfpVcatHeader_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notApplicable',1),(_P,2),(_Q,3)))
_GfpVcatHeader_Type.__name__=_D
_GfpVcatHeader_Object=MibTableColumn
gfpVcatHeader=_GfpVcatHeader_Object((1,3,6,1,4,1,164,6,2,55,1,1,4),_GfpVcatHeader_Type())
gfpVcatHeader.setMaxAccess(_L)
if mibBuilder.loadTexts:gfpVcatHeader.setStatus(_B)
gfpLof=NotificationType((1,3,6,1,4,1,164,6,2,55,0,1))
gfpLof.setObjects(*((_A,_J),(_A,_F),(_A,_H),(_A,_I),(_A,_G),(_A,_K),(_C,_E)))
if mibBuilder.loadTexts:gfpLof.setStatus(_B)
gfpCsf=NotificationType((1,3,6,1,4,1,164,6,2,55,0,2))
gfpCsf.setObjects(*((_A,_J),(_A,_F),(_A,_H),(_A,_I),(_A,_G),(_A,_K),(_C,_E)))
if mibBuilder.loadTexts:gfpCsf.setStatus(_B)
mibBuilder.exportSymbols(_N,**{'gfp':gfp,'gfpEvents':gfpEvents,'gfpLof':gfpLof,'gfpCsf':gfpCsf,'gfpCnfgTable':gfpCnfgTable,'gfpCnfgEntry':gfpCnfgEntry,_O:gfpCnfgIdx,'gfpPayloadFcs':gfpPayloadFcs,'gfpRxTxScramble':gfpRxTxScramble,'gfpVcatHeader':gfpVcatHeader})