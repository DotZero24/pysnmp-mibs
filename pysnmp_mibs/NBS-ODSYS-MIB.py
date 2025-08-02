_X='nbsOdsysChasIndex'
_W='nbsOdsysPsIOutLevel'
_V='nbsOdsysPsIOutActual'
_U='nbsOdsysPsIInLevel'
_T='nbsOdsysPsIInActual'
_S='nbsOdsysPsVOutLevel'
_R='nbsOdsysPsVOutActual'
_Q='nbsOdsysPsVInLevel'
_P='nbsOdsysPsVInActual'
_O='nbsOdsysPsThermLevel'
_N='nbsOdsysPsThermActual'
_M='nbsOdsysFtThermLevel'
_L='nbsOdsysFtThermActual'
_K='nbsOdsysCcThermLevel'
_J='nbsOdsysCcThermActual'
_I='nbsOdsysFtBayIndex'
_H='nbsOdsysFtChasIndex'
_G='nbsOdsysCcBayIndex'
_F='nbsOdsysCcChasIndex'
_E='nbsOdsysPsBayIndex'
_D='nbsOdsysPsChasIndex'
_C='read-only'
_B='NBS-ODSYS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
NbsTcMilliAmp,NbsTcMilliVolt,NbsTcPartIndex,NbsTcStatusLevel,NbsTcStatusSimple,NbsTcTemperature,nbs=mibBuilder.importSymbols('NBS-MIB','NbsTcMilliAmp','NbsTcMilliVolt','NbsTcPartIndex','NbsTcStatusLevel','NbsTcStatusSimple','NbsTcTemperature','nbs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
nbsOdsysMib=ModuleIdentity((1,3,6,1,4,1,629,228))
_NbsOdsysChasGrp_ObjectIdentity=ObjectIdentity
nbsOdsysChasGrp=_NbsOdsysChasGrp_ObjectIdentity((1,3,6,1,4,1,629,228,2))
if mibBuilder.loadTexts:nbsOdsysChasGrp.setStatus(_A)
_NbsOdsysChasTable_Object=MibTable
nbsOdsysChasTable=_NbsOdsysChasTable_Object((1,3,6,1,4,1,629,228,2,1))
if mibBuilder.loadTexts:nbsOdsysChasTable.setStatus(_A)
_NbsOdsysChasEntry_Object=MibTableRow
nbsOdsysChasEntry=_NbsOdsysChasEntry_Object((1,3,6,1,4,1,629,228,2,1,1))
nbsOdsysChasEntry.setIndexNames((0,_B,_X))
if mibBuilder.loadTexts:nbsOdsysChasEntry.setStatus(_A)
_NbsOdsysChasIndex_Type=Integer32
_NbsOdsysChasIndex_Object=MibTableColumn
nbsOdsysChasIndex=_NbsOdsysChasIndex_Object((1,3,6,1,4,1,629,228,2,1,1,1),_NbsOdsysChasIndex_Type())
nbsOdsysChasIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysChasIndex.setStatus(_A)
_NbsOdsysChasCcMaxCount_Type=Integer32
_NbsOdsysChasCcMaxCount_Object=MibTableColumn
nbsOdsysChasCcMaxCount=_NbsOdsysChasCcMaxCount_Object((1,3,6,1,4,1,629,228,2,1,1,10),_NbsOdsysChasCcMaxCount_Type())
nbsOdsysChasCcMaxCount.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysChasCcMaxCount.setStatus(_A)
_NbsOdsysChasPsMaxCount_Type=Integer32
_NbsOdsysChasPsMaxCount_Object=MibTableColumn
nbsOdsysChasPsMaxCount=_NbsOdsysChasPsMaxCount_Object((1,3,6,1,4,1,629,228,2,1,1,20),_NbsOdsysChasPsMaxCount_Type())
nbsOdsysChasPsMaxCount.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysChasPsMaxCount.setStatus(_A)
_NbsOdsysChasFtMaxCount_Type=Integer32
_NbsOdsysChasFtMaxCount_Object=MibTableColumn
nbsOdsysChasFtMaxCount=_NbsOdsysChasFtMaxCount_Object((1,3,6,1,4,1,629,228,2,1,1,30),_NbsOdsysChasFtMaxCount_Type())
nbsOdsysChasFtMaxCount.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysChasFtMaxCount.setStatus(_A)
_NbsOdsysCcGrp_ObjectIdentity=ObjectIdentity
nbsOdsysCcGrp=_NbsOdsysCcGrp_ObjectIdentity((1,3,6,1,4,1,629,228,3))
if mibBuilder.loadTexts:nbsOdsysCcGrp.setStatus(_A)
_NbsOdsysCcTable_Object=MibTable
nbsOdsysCcTable=_NbsOdsysCcTable_Object((1,3,6,1,4,1,629,228,3,1))
if mibBuilder.loadTexts:nbsOdsysCcTable.setStatus(_A)
_NbsOdsysCcEntry_Object=MibTableRow
nbsOdsysCcEntry=_NbsOdsysCcEntry_Object((1,3,6,1,4,1,629,228,3,1,1))
nbsOdsysCcEntry.setIndexNames((0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:nbsOdsysCcEntry.setStatus(_A)
_NbsOdsysCcChasIndex_Type=Integer32
_NbsOdsysCcChasIndex_Object=MibTableColumn
nbsOdsysCcChasIndex=_NbsOdsysCcChasIndex_Object((1,3,6,1,4,1,629,228,3,1,1,1),_NbsOdsysCcChasIndex_Type())
nbsOdsysCcChasIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysCcChasIndex.setStatus(_A)
_NbsOdsysCcBayIndex_Type=Integer32
_NbsOdsysCcBayIndex_Object=MibTableColumn
nbsOdsysCcBayIndex=_NbsOdsysCcBayIndex_Object((1,3,6,1,4,1,629,228,3,1,1,2),_NbsOdsysCcBayIndex_Type())
nbsOdsysCcBayIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysCcBayIndex.setStatus(_A)
_NbsOdsysCcChIfIndex_Type=InterfaceIndex
_NbsOdsysCcChIfIndex_Object=MibTableColumn
nbsOdsysCcChIfIndex=_NbsOdsysCcChIfIndex_Object((1,3,6,1,4,1,629,228,3,1,1,10),_NbsOdsysCcChIfIndex_Type())
nbsOdsysCcChIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysCcChIfIndex.setStatus(_A)
_NbsOdsysCcPartIndex_Type=NbsTcPartIndex
_NbsOdsysCcPartIndex_Object=MibTableColumn
nbsOdsysCcPartIndex=_NbsOdsysCcPartIndex_Object((1,3,6,1,4,1,629,228,3,1,1,11),_NbsOdsysCcPartIndex_Type())
nbsOdsysCcPartIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysCcPartIndex.setStatus(_A)
_NbsOdsysCcThermActual_Type=NbsTcTemperature
_NbsOdsysCcThermActual_Object=MibTableColumn
nbsOdsysCcThermActual=_NbsOdsysCcThermActual_Object((1,3,6,1,4,1,629,228,3,1,1,30),_NbsOdsysCcThermActual_Type())
nbsOdsysCcThermActual.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysCcThermActual.setStatus(_A)
_NbsOdsysCcThermLevel_Type=NbsTcStatusLevel
_NbsOdsysCcThermLevel_Object=MibTableColumn
nbsOdsysCcThermLevel=_NbsOdsysCcThermLevel_Object((1,3,6,1,4,1,629,228,3,1,1,40),_NbsOdsysCcThermLevel_Type())
nbsOdsysCcThermLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysCcThermLevel.setStatus(_A)
_NbsOdsysCcThermThreshLoErr_Type=NbsTcTemperature
_NbsOdsysCcThermThreshLoErr_Object=MibTableColumn
nbsOdsysCcThermThreshLoErr=_NbsOdsysCcThermThreshLoErr_Object((1,3,6,1,4,1,629,228,3,1,1,41),_NbsOdsysCcThermThreshLoErr_Type())
nbsOdsysCcThermThreshLoErr.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysCcThermThreshLoErr.setStatus(_A)
_NbsOdsysCcThermThreshLoWarn_Type=NbsTcTemperature
_NbsOdsysCcThermThreshLoWarn_Object=MibTableColumn
nbsOdsysCcThermThreshLoWarn=_NbsOdsysCcThermThreshLoWarn_Object((1,3,6,1,4,1,629,228,3,1,1,42),_NbsOdsysCcThermThreshLoWarn_Type())
nbsOdsysCcThermThreshLoWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysCcThermThreshLoWarn.setStatus(_A)
_NbsOdsysCcThermThreshHiWarn_Type=NbsTcTemperature
_NbsOdsysCcThermThreshHiWarn_Object=MibTableColumn
nbsOdsysCcThermThreshHiWarn=_NbsOdsysCcThermThreshHiWarn_Object((1,3,6,1,4,1,629,228,3,1,1,43),_NbsOdsysCcThermThreshHiWarn_Type())
nbsOdsysCcThermThreshHiWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysCcThermThreshHiWarn.setStatus(_A)
_NbsOdsysCcThermThreshHiErr_Type=NbsTcTemperature
_NbsOdsysCcThermThreshHiErr_Object=MibTableColumn
nbsOdsysCcThermThreshHiErr=_NbsOdsysCcThermThreshHiErr_Object((1,3,6,1,4,1,629,228,3,1,1,44),_NbsOdsysCcThermThreshHiErr_Type())
nbsOdsysCcThermThreshHiErr.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysCcThermThreshHiErr.setStatus(_A)
_NbsOdsysCcOperationalStatus_Type=NbsTcStatusSimple
_NbsOdsysCcOperationalStatus_Object=MibTableColumn
nbsOdsysCcOperationalStatus=_NbsOdsysCcOperationalStatus_Object((1,3,6,1,4,1,629,228,3,1,1,50),_NbsOdsysCcOperationalStatus_Type())
nbsOdsysCcOperationalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysCcOperationalStatus.setStatus(_A)
_NbsOdsysFtGrp_ObjectIdentity=ObjectIdentity
nbsOdsysFtGrp=_NbsOdsysFtGrp_ObjectIdentity((1,3,6,1,4,1,629,228,4))
if mibBuilder.loadTexts:nbsOdsysFtGrp.setStatus(_A)
_NbsOdsysFtTable_Object=MibTable
nbsOdsysFtTable=_NbsOdsysFtTable_Object((1,3,6,1,4,1,629,228,4,1))
if mibBuilder.loadTexts:nbsOdsysFtTable.setStatus(_A)
_NbsOdsysFtEntry_Object=MibTableRow
nbsOdsysFtEntry=_NbsOdsysFtEntry_Object((1,3,6,1,4,1,629,228,4,1,1))
nbsOdsysFtEntry.setIndexNames((0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:nbsOdsysFtEntry.setStatus(_A)
_NbsOdsysFtChasIndex_Type=Integer32
_NbsOdsysFtChasIndex_Object=MibTableColumn
nbsOdsysFtChasIndex=_NbsOdsysFtChasIndex_Object((1,3,6,1,4,1,629,228,4,1,1,1),_NbsOdsysFtChasIndex_Type())
nbsOdsysFtChasIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysFtChasIndex.setStatus(_A)
_NbsOdsysFtBayIndex_Type=Integer32
_NbsOdsysFtBayIndex_Object=MibTableColumn
nbsOdsysFtBayIndex=_NbsOdsysFtBayIndex_Object((1,3,6,1,4,1,629,228,4,1,1,2),_NbsOdsysFtBayIndex_Type())
nbsOdsysFtBayIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysFtBayIndex.setStatus(_A)
_NbsOdsysFtOperationalStatus_Type=NbsTcStatusSimple
_NbsOdsysFtOperationalStatus_Object=MibTableColumn
nbsOdsysFtOperationalStatus=_NbsOdsysFtOperationalStatus_Object((1,3,6,1,4,1,629,228,4,1,1,3),_NbsOdsysFtOperationalStatus_Type())
nbsOdsysFtOperationalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysFtOperationalStatus.setStatus(_A)
_NbsOdsysFtChIfIndex_Type=InterfaceIndex
_NbsOdsysFtChIfIndex_Object=MibTableColumn
nbsOdsysFtChIfIndex=_NbsOdsysFtChIfIndex_Object((1,3,6,1,4,1,629,228,4,1,1,10),_NbsOdsysFtChIfIndex_Type())
nbsOdsysFtChIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysFtChIfIndex.setStatus(_A)
_NbsOdsysFtPartIndex_Type=NbsTcPartIndex
_NbsOdsysFtPartIndex_Object=MibTableColumn
nbsOdsysFtPartIndex=_NbsOdsysFtPartIndex_Object((1,3,6,1,4,1,629,228,4,1,1,11),_NbsOdsysFtPartIndex_Type())
nbsOdsysFtPartIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysFtPartIndex.setStatus(_A)
_NbsOdsysFtFanCount_Type=Integer32
_NbsOdsysFtFanCount_Object=MibTableColumn
nbsOdsysFtFanCount=_NbsOdsysFtFanCount_Object((1,3,6,1,4,1,629,228,4,1,1,20),_NbsOdsysFtFanCount_Type())
nbsOdsysFtFanCount.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysFtFanCount.setStatus(_A)
_NbsOdsysFtThermActual_Type=NbsTcTemperature
_NbsOdsysFtThermActual_Object=MibTableColumn
nbsOdsysFtThermActual=_NbsOdsysFtThermActual_Object((1,3,6,1,4,1,629,228,4,1,1,30),_NbsOdsysFtThermActual_Type())
nbsOdsysFtThermActual.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysFtThermActual.setStatus(_A)
_NbsOdsysFtThermLevel_Type=NbsTcStatusLevel
_NbsOdsysFtThermLevel_Object=MibTableColumn
nbsOdsysFtThermLevel=_NbsOdsysFtThermLevel_Object((1,3,6,1,4,1,629,228,4,1,1,40),_NbsOdsysFtThermLevel_Type())
nbsOdsysFtThermLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysFtThermLevel.setStatus(_A)
_NbsOdsysFtThermThreshLoErr_Type=NbsTcTemperature
_NbsOdsysFtThermThreshLoErr_Object=MibTableColumn
nbsOdsysFtThermThreshLoErr=_NbsOdsysFtThermThreshLoErr_Object((1,3,6,1,4,1,629,228,4,1,1,41),_NbsOdsysFtThermThreshLoErr_Type())
nbsOdsysFtThermThreshLoErr.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysFtThermThreshLoErr.setStatus(_A)
_NbsOdsysFtThermThreshLoWarn_Type=NbsTcTemperature
_NbsOdsysFtThermThreshLoWarn_Object=MibTableColumn
nbsOdsysFtThermThreshLoWarn=_NbsOdsysFtThermThreshLoWarn_Object((1,3,6,1,4,1,629,228,4,1,1,42),_NbsOdsysFtThermThreshLoWarn_Type())
nbsOdsysFtThermThreshLoWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysFtThermThreshLoWarn.setStatus(_A)
_NbsOdsysFtThermThreshHiWarn_Type=NbsTcTemperature
_NbsOdsysFtThermThreshHiWarn_Object=MibTableColumn
nbsOdsysFtThermThreshHiWarn=_NbsOdsysFtThermThreshHiWarn_Object((1,3,6,1,4,1,629,228,4,1,1,43),_NbsOdsysFtThermThreshHiWarn_Type())
nbsOdsysFtThermThreshHiWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysFtThermThreshHiWarn.setStatus(_A)
_NbsOdsysFtThermThreshHiErr_Type=NbsTcTemperature
_NbsOdsysFtThermThreshHiErr_Object=MibTableColumn
nbsOdsysFtThermThreshHiErr=_NbsOdsysFtThermThreshHiErr_Object((1,3,6,1,4,1,629,228,4,1,1,44),_NbsOdsysFtThermThreshHiErr_Type())
nbsOdsysFtThermThreshHiErr.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysFtThermThreshHiErr.setStatus(_A)
_NbsOdsysPsGrp_ObjectIdentity=ObjectIdentity
nbsOdsysPsGrp=_NbsOdsysPsGrp_ObjectIdentity((1,3,6,1,4,1,629,228,5))
if mibBuilder.loadTexts:nbsOdsysPsGrp.setStatus(_A)
_NbsOdsysPsTable_Object=MibTable
nbsOdsysPsTable=_NbsOdsysPsTable_Object((1,3,6,1,4,1,629,228,5,2))
if mibBuilder.loadTexts:nbsOdsysPsTable.setStatus(_A)
_NbsOdsysPsEntry_Object=MibTableRow
nbsOdsysPsEntry=_NbsOdsysPsEntry_Object((1,3,6,1,4,1,629,228,5,2,1))
nbsOdsysPsEntry.setIndexNames((0,_B,_D),(0,_B,_E))
if mibBuilder.loadTexts:nbsOdsysPsEntry.setStatus(_A)
_NbsOdsysPsChasIndex_Type=Integer32
_NbsOdsysPsChasIndex_Object=MibTableColumn
nbsOdsysPsChasIndex=_NbsOdsysPsChasIndex_Object((1,3,6,1,4,1,629,228,5,2,1,1),_NbsOdsysPsChasIndex_Type())
nbsOdsysPsChasIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysPsChasIndex.setStatus(_A)
_NbsOdsysPsBayIndex_Type=Integer32
_NbsOdsysPsBayIndex_Object=MibTableColumn
nbsOdsysPsBayIndex=_NbsOdsysPsBayIndex_Object((1,3,6,1,4,1,629,228,5,2,1,2),_NbsOdsysPsBayIndex_Type())
nbsOdsysPsBayIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysPsBayIndex.setStatus(_A)
_NbsOdsysPsOperationalStatus_Type=NbsTcStatusSimple
_NbsOdsysPsOperationalStatus_Object=MibTableColumn
nbsOdsysPsOperationalStatus=_NbsOdsysPsOperationalStatus_Object((1,3,6,1,4,1,629,228,5,2,1,3),_NbsOdsysPsOperationalStatus_Type())
nbsOdsysPsOperationalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysPsOperationalStatus.setStatus(_A)
_NbsOdsysPsChIfIndex_Type=InterfaceIndex
_NbsOdsysPsChIfIndex_Object=MibTableColumn
nbsOdsysPsChIfIndex=_NbsOdsysPsChIfIndex_Object((1,3,6,1,4,1,629,228,5,2,1,10),_NbsOdsysPsChIfIndex_Type())
nbsOdsysPsChIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysPsChIfIndex.setStatus(_A)
_NbsOdsysPsPartIndex_Type=NbsTcPartIndex
_NbsOdsysPsPartIndex_Object=MibTableColumn
nbsOdsysPsPartIndex=_NbsOdsysPsPartIndex_Object((1,3,6,1,4,1,629,228,5,2,1,11),_NbsOdsysPsPartIndex_Type())
nbsOdsysPsPartIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysPsPartIndex.setStatus(_A)
_NbsOdsysPsFanCount_Type=Integer32
_NbsOdsysPsFanCount_Object=MibTableColumn
nbsOdsysPsFanCount=_NbsOdsysPsFanCount_Object((1,3,6,1,4,1,629,228,5,2,1,30),_NbsOdsysPsFanCount_Type())
nbsOdsysPsFanCount.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysPsFanCount.setStatus(_A)
_NbsOdsysPsThermActual_Type=NbsTcTemperature
_NbsOdsysPsThermActual_Object=MibTableColumn
nbsOdsysPsThermActual=_NbsOdsysPsThermActual_Object((1,3,6,1,4,1,629,228,5,2,1,40),_NbsOdsysPsThermActual_Type())
nbsOdsysPsThermActual.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysPsThermActual.setStatus(_A)
_NbsOdsysPsThermLevel_Type=NbsTcStatusLevel
_NbsOdsysPsThermLevel_Object=MibTableColumn
nbsOdsysPsThermLevel=_NbsOdsysPsThermLevel_Object((1,3,6,1,4,1,629,228,5,2,1,41),_NbsOdsysPsThermLevel_Type())
nbsOdsysPsThermLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysPsThermLevel.setStatus(_A)
_NbsOdsysPsThermThreshLoErr_Type=NbsTcTemperature
_NbsOdsysPsThermThreshLoErr_Object=MibTableColumn
nbsOdsysPsThermThreshLoErr=_NbsOdsysPsThermThreshLoErr_Object((1,3,6,1,4,1,629,228,5,2,1,42),_NbsOdsysPsThermThreshLoErr_Type())
nbsOdsysPsThermThreshLoErr.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysPsThermThreshLoErr.setStatus(_A)
_NbsOdsysPsThermThreshLoWarn_Type=NbsTcTemperature
_NbsOdsysPsThermThreshLoWarn_Object=MibTableColumn
nbsOdsysPsThermThreshLoWarn=_NbsOdsysPsThermThreshLoWarn_Object((1,3,6,1,4,1,629,228,5,2,1,43),_NbsOdsysPsThermThreshLoWarn_Type())
nbsOdsysPsThermThreshLoWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysPsThermThreshLoWarn.setStatus(_A)
_NbsOdsysPsThermThreshHiWarn_Type=NbsTcTemperature
_NbsOdsysPsThermThreshHiWarn_Object=MibTableColumn
nbsOdsysPsThermThreshHiWarn=_NbsOdsysPsThermThreshHiWarn_Object((1,3,6,1,4,1,629,228,5,2,1,44),_NbsOdsysPsThermThreshHiWarn_Type())
nbsOdsysPsThermThreshHiWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysPsThermThreshHiWarn.setStatus(_A)
_NbsOdsysPsThermThreshHiErr_Type=NbsTcTemperature
_NbsOdsysPsThermThreshHiErr_Object=MibTableColumn
nbsOdsysPsThermThreshHiErr=_NbsOdsysPsThermThreshHiErr_Object((1,3,6,1,4,1,629,228,5,2,1,45),_NbsOdsysPsThermThreshHiErr_Type())
nbsOdsysPsThermThreshHiErr.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysPsThermThreshHiErr.setStatus(_A)
_NbsOdsysPsVInActual_Type=NbsTcMilliVolt
_NbsOdsysPsVInActual_Object=MibTableColumn
nbsOdsysPsVInActual=_NbsOdsysPsVInActual_Object((1,3,6,1,4,1,629,228,5,2,1,50),_NbsOdsysPsVInActual_Type())
nbsOdsysPsVInActual.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysPsVInActual.setStatus(_A)
_NbsOdsysPsVInLevel_Type=NbsTcStatusLevel
_NbsOdsysPsVInLevel_Object=MibTableColumn
nbsOdsysPsVInLevel=_NbsOdsysPsVInLevel_Object((1,3,6,1,4,1,629,228,5,2,1,51),_NbsOdsysPsVInLevel_Type())
nbsOdsysPsVInLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysPsVInLevel.setStatus(_A)
_NbsOdsysPsVInThreshLoErr_Type=NbsTcMilliVolt
_NbsOdsysPsVInThreshLoErr_Object=MibTableColumn
nbsOdsysPsVInThreshLoErr=_NbsOdsysPsVInThreshLoErr_Object((1,3,6,1,4,1,629,228,5,2,1,52),_NbsOdsysPsVInThreshLoErr_Type())
nbsOdsysPsVInThreshLoErr.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysPsVInThreshLoErr.setStatus(_A)
_NbsOdsysPsVInThreshLoWarn_Type=NbsTcMilliVolt
_NbsOdsysPsVInThreshLoWarn_Object=MibTableColumn
nbsOdsysPsVInThreshLoWarn=_NbsOdsysPsVInThreshLoWarn_Object((1,3,6,1,4,1,629,228,5,2,1,53),_NbsOdsysPsVInThreshLoWarn_Type())
nbsOdsysPsVInThreshLoWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysPsVInThreshLoWarn.setStatus(_A)
_NbsOdsysPsVInThreshHiWarn_Type=NbsTcMilliVolt
_NbsOdsysPsVInThreshHiWarn_Object=MibTableColumn
nbsOdsysPsVInThreshHiWarn=_NbsOdsysPsVInThreshHiWarn_Object((1,3,6,1,4,1,629,228,5,2,1,54),_NbsOdsysPsVInThreshHiWarn_Type())
nbsOdsysPsVInThreshHiWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysPsVInThreshHiWarn.setStatus(_A)
_NbsOdsysPsVInThreshHiErr_Type=NbsTcMilliVolt
_NbsOdsysPsVInThreshHiErr_Object=MibTableColumn
nbsOdsysPsVInThreshHiErr=_NbsOdsysPsVInThreshHiErr_Object((1,3,6,1,4,1,629,228,5,2,1,55),_NbsOdsysPsVInThreshHiErr_Type())
nbsOdsysPsVInThreshHiErr.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysPsVInThreshHiErr.setStatus(_A)
_NbsOdsysPsVOutActual_Type=NbsTcMilliVolt
_NbsOdsysPsVOutActual_Object=MibTableColumn
nbsOdsysPsVOutActual=_NbsOdsysPsVOutActual_Object((1,3,6,1,4,1,629,228,5,2,1,60),_NbsOdsysPsVOutActual_Type())
nbsOdsysPsVOutActual.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysPsVOutActual.setStatus(_A)
_NbsOdsysPsVOutLevel_Type=NbsTcStatusLevel
_NbsOdsysPsVOutLevel_Object=MibTableColumn
nbsOdsysPsVOutLevel=_NbsOdsysPsVOutLevel_Object((1,3,6,1,4,1,629,228,5,2,1,61),_NbsOdsysPsVOutLevel_Type())
nbsOdsysPsVOutLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysPsVOutLevel.setStatus(_A)
_NbsOdsysPsVOutThreshLoErr_Type=NbsTcMilliVolt
_NbsOdsysPsVOutThreshLoErr_Object=MibTableColumn
nbsOdsysPsVOutThreshLoErr=_NbsOdsysPsVOutThreshLoErr_Object((1,3,6,1,4,1,629,228,5,2,1,62),_NbsOdsysPsVOutThreshLoErr_Type())
nbsOdsysPsVOutThreshLoErr.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysPsVOutThreshLoErr.setStatus(_A)
_NbsOdsysPsVOutThreshLoWarn_Type=NbsTcMilliVolt
_NbsOdsysPsVOutThreshLoWarn_Object=MibTableColumn
nbsOdsysPsVOutThreshLoWarn=_NbsOdsysPsVOutThreshLoWarn_Object((1,3,6,1,4,1,629,228,5,2,1,63),_NbsOdsysPsVOutThreshLoWarn_Type())
nbsOdsysPsVOutThreshLoWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysPsVOutThreshLoWarn.setStatus(_A)
_NbsOdsysPsVOutThreshHiWarn_Type=NbsTcMilliVolt
_NbsOdsysPsVOutThreshHiWarn_Object=MibTableColumn
nbsOdsysPsVOutThreshHiWarn=_NbsOdsysPsVOutThreshHiWarn_Object((1,3,6,1,4,1,629,228,5,2,1,64),_NbsOdsysPsVOutThreshHiWarn_Type())
nbsOdsysPsVOutThreshHiWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysPsVOutThreshHiWarn.setStatus(_A)
_NbsOdsysPsVOutThreshHiErr_Type=NbsTcMilliVolt
_NbsOdsysPsVOutThreshHiErr_Object=MibTableColumn
nbsOdsysPsVOutThreshHiErr=_NbsOdsysPsVOutThreshHiErr_Object((1,3,6,1,4,1,629,228,5,2,1,65),_NbsOdsysPsVOutThreshHiErr_Type())
nbsOdsysPsVOutThreshHiErr.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysPsVOutThreshHiErr.setStatus(_A)
_NbsOdsysPsIInActual_Type=NbsTcMilliAmp
_NbsOdsysPsIInActual_Object=MibTableColumn
nbsOdsysPsIInActual=_NbsOdsysPsIInActual_Object((1,3,6,1,4,1,629,228,5,2,1,70),_NbsOdsysPsIInActual_Type())
nbsOdsysPsIInActual.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysPsIInActual.setStatus(_A)
_NbsOdsysPsIInLevel_Type=NbsTcStatusLevel
_NbsOdsysPsIInLevel_Object=MibTableColumn
nbsOdsysPsIInLevel=_NbsOdsysPsIInLevel_Object((1,3,6,1,4,1,629,228,5,2,1,71),_NbsOdsysPsIInLevel_Type())
nbsOdsysPsIInLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysPsIInLevel.setStatus(_A)
_NbsOdsysPsIInThreshLoErr_Type=NbsTcMilliAmp
_NbsOdsysPsIInThreshLoErr_Object=MibTableColumn
nbsOdsysPsIInThreshLoErr=_NbsOdsysPsIInThreshLoErr_Object((1,3,6,1,4,1,629,228,5,2,1,72),_NbsOdsysPsIInThreshLoErr_Type())
nbsOdsysPsIInThreshLoErr.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysPsIInThreshLoErr.setStatus(_A)
_NbsOdsysPsIInThreshLoWarn_Type=NbsTcMilliAmp
_NbsOdsysPsIInThreshLoWarn_Object=MibTableColumn
nbsOdsysPsIInThreshLoWarn=_NbsOdsysPsIInThreshLoWarn_Object((1,3,6,1,4,1,629,228,5,2,1,73),_NbsOdsysPsIInThreshLoWarn_Type())
nbsOdsysPsIInThreshLoWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysPsIInThreshLoWarn.setStatus(_A)
_NbsOdsysPsIInThreshHiWarn_Type=NbsTcMilliAmp
_NbsOdsysPsIInThreshHiWarn_Object=MibTableColumn
nbsOdsysPsIInThreshHiWarn=_NbsOdsysPsIInThreshHiWarn_Object((1,3,6,1,4,1,629,228,5,2,1,74),_NbsOdsysPsIInThreshHiWarn_Type())
nbsOdsysPsIInThreshHiWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysPsIInThreshHiWarn.setStatus(_A)
_NbsOdsysPsIInThreshHiErr_Type=NbsTcMilliAmp
_NbsOdsysPsIInThreshHiErr_Object=MibTableColumn
nbsOdsysPsIInThreshHiErr=_NbsOdsysPsIInThreshHiErr_Object((1,3,6,1,4,1,629,228,5,2,1,75),_NbsOdsysPsIInThreshHiErr_Type())
nbsOdsysPsIInThreshHiErr.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysPsIInThreshHiErr.setStatus(_A)
_NbsOdsysPsIOutActual_Type=NbsTcMilliAmp
_NbsOdsysPsIOutActual_Object=MibTableColumn
nbsOdsysPsIOutActual=_NbsOdsysPsIOutActual_Object((1,3,6,1,4,1,629,228,5,2,1,80),_NbsOdsysPsIOutActual_Type())
nbsOdsysPsIOutActual.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysPsIOutActual.setStatus(_A)
_NbsOdsysPsIOutLevel_Type=NbsTcStatusLevel
_NbsOdsysPsIOutLevel_Object=MibTableColumn
nbsOdsysPsIOutLevel=_NbsOdsysPsIOutLevel_Object((1,3,6,1,4,1,629,228,5,2,1,81),_NbsOdsysPsIOutLevel_Type())
nbsOdsysPsIOutLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysPsIOutLevel.setStatus(_A)
_NbsOdsysPsIOutThreshLoErr_Type=NbsTcMilliAmp
_NbsOdsysPsIOutThreshLoErr_Object=MibTableColumn
nbsOdsysPsIOutThreshLoErr=_NbsOdsysPsIOutThreshLoErr_Object((1,3,6,1,4,1,629,228,5,2,1,82),_NbsOdsysPsIOutThreshLoErr_Type())
nbsOdsysPsIOutThreshLoErr.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysPsIOutThreshLoErr.setStatus(_A)
_NbsOdsysPsIOutThreshLoWarn_Type=NbsTcMilliAmp
_NbsOdsysPsIOutThreshLoWarn_Object=MibTableColumn
nbsOdsysPsIOutThreshLoWarn=_NbsOdsysPsIOutThreshLoWarn_Object((1,3,6,1,4,1,629,228,5,2,1,83),_NbsOdsysPsIOutThreshLoWarn_Type())
nbsOdsysPsIOutThreshLoWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysPsIOutThreshLoWarn.setStatus(_A)
_NbsOdsysPsIOutThreshHiWarn_Type=NbsTcMilliAmp
_NbsOdsysPsIOutThreshHiWarn_Object=MibTableColumn
nbsOdsysPsIOutThreshHiWarn=_NbsOdsysPsIOutThreshHiWarn_Object((1,3,6,1,4,1,629,228,5,2,1,84),_NbsOdsysPsIOutThreshHiWarn_Type())
nbsOdsysPsIOutThreshHiWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysPsIOutThreshHiWarn.setStatus(_A)
_NbsOdsysPsIOutThreshHiErr_Type=NbsTcMilliAmp
_NbsOdsysPsIOutThreshHiErr_Object=MibTableColumn
nbsOdsysPsIOutThreshHiErr=_NbsOdsysPsIOutThreshHiErr_Object((1,3,6,1,4,1,629,228,5,2,1,85),_NbsOdsysPsIOutThreshHiErr_Type())
nbsOdsysPsIOutThreshHiErr.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOdsysPsIOutThreshHiErr.setStatus(_A)
_NbsOdsysEventsGrp_ObjectIdentity=ObjectIdentity
nbsOdsysEventsGrp=_NbsOdsysEventsGrp_ObjectIdentity((1,3,6,1,4,1,629,228,100))
if mibBuilder.loadTexts:nbsOdsysEventsGrp.setStatus(_A)
_NbsOdsysEvents_ObjectIdentity=ObjectIdentity
nbsOdsysEvents=_NbsOdsysEvents_ObjectIdentity((1,3,6,1,4,1,629,228,100,0))
if mibBuilder.loadTexts:nbsOdsysEvents.setStatus(_A)
nbsOdsysTrapCcThermLevelBad=NotificationType((1,3,6,1,4,1,629,228,100,0,30))
nbsOdsysTrapCcThermLevelBad.setObjects(*((_B,_F),(_B,_G),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:nbsOdsysTrapCcThermLevelBad.setStatus(_A)
nbsOdsysTrapCcThermLevelOk=NotificationType((1,3,6,1,4,1,629,228,100,0,31))
nbsOdsysTrapCcThermLevelOk.setObjects(*((_B,_F),(_B,_G),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:nbsOdsysTrapCcThermLevelOk.setStatus(_A)
nbsOdsysTrapFtThermLevelBad=NotificationType((1,3,6,1,4,1,629,228,100,0,40))
nbsOdsysTrapFtThermLevelBad.setObjects(*((_B,_H),(_B,_I),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:nbsOdsysTrapFtThermLevelBad.setStatus(_A)
nbsOdsysTrapFtThermLevelOk=NotificationType((1,3,6,1,4,1,629,228,100,0,41))
nbsOdsysTrapFtThermLevelOk.setObjects(*((_B,_H),(_B,_I),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:nbsOdsysTrapFtThermLevelOk.setStatus(_A)
nbsOdsysTrapPsThermLevelBad=NotificationType((1,3,6,1,4,1,629,228,100,0,50))
nbsOdsysTrapPsThermLevelBad.setObjects(*((_B,_D),(_B,_E),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:nbsOdsysTrapPsThermLevelBad.setStatus(_A)
nbsOdsysTrapPsThermLevelOk=NotificationType((1,3,6,1,4,1,629,228,100,0,51))
nbsOdsysTrapPsThermLevelOk.setObjects(*((_B,_D),(_B,_E),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:nbsOdsysTrapPsThermLevelOk.setStatus(_A)
nbsOdsysTrapPsVInLevelBad=NotificationType((1,3,6,1,4,1,629,228,100,0,60))
nbsOdsysTrapPsVInLevelBad.setObjects(*((_B,_D),(_B,_E),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:nbsOdsysTrapPsVInLevelBad.setStatus(_A)
nbsOdsysTrapPsVInLevelOk=NotificationType((1,3,6,1,4,1,629,228,100,0,61))
nbsOdsysTrapPsVInLevelOk.setObjects(*((_B,_D),(_B,_E),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:nbsOdsysTrapPsVInLevelOk.setStatus(_A)
nbsOdsysTrapPsVOutLevelBad=NotificationType((1,3,6,1,4,1,629,228,100,0,70))
nbsOdsysTrapPsVOutLevelBad.setObjects(*((_B,_D),(_B,_E),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:nbsOdsysTrapPsVOutLevelBad.setStatus(_A)
nbsOdsysTrapPsVOutLevelOk=NotificationType((1,3,6,1,4,1,629,228,100,0,71))
nbsOdsysTrapPsVOutLevelOk.setObjects(*((_B,_D),(_B,_E),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:nbsOdsysTrapPsVOutLevelOk.setStatus(_A)
nbsOdsysTrapPsIInLevelBad=NotificationType((1,3,6,1,4,1,629,228,100,0,80))
nbsOdsysTrapPsIInLevelBad.setObjects(*((_B,_D),(_B,_E),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:nbsOdsysTrapPsIInLevelBad.setStatus(_A)
nbsOdsysTrapPsIInLevelOk=NotificationType((1,3,6,1,4,1,629,228,100,0,81))
nbsOdsysTrapPsIInLevelOk.setObjects(*((_B,_D),(_B,_E),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:nbsOdsysTrapPsIInLevelOk.setStatus(_A)
nbsOdsysTrapPsIOutLevelBad=NotificationType((1,3,6,1,4,1,629,228,100,0,90))
nbsOdsysTrapPsIOutLevelBad.setObjects(*((_B,_D),(_B,_E),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:nbsOdsysTrapPsIOutLevelBad.setStatus(_A)
nbsOdsysTrapPsIOutLevelOk=NotificationType((1,3,6,1,4,1,629,228,100,0,91))
nbsOdsysTrapPsIOutLevelOk.setObjects(*((_B,_D),(_B,_E),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:nbsOdsysTrapPsIOutLevelOk.setStatus(_A)
nbsOdsysTrapCcFailed=NotificationType((1,3,6,1,4,1,629,228,100,0,131))
nbsOdsysTrapCcFailed.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:nbsOdsysTrapCcFailed.setStatus(_A)
nbsOdsysTrapCcRestored=NotificationType((1,3,6,1,4,1,629,228,100,0,132))
nbsOdsysTrapCcRestored.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:nbsOdsysTrapCcRestored.setStatus(_A)
nbsOdsysTrapCcRemoved=NotificationType((1,3,6,1,4,1,629,228,100,0,133))
nbsOdsysTrapCcRemoved.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:nbsOdsysTrapCcRemoved.setStatus(_A)
nbsOdsysTrapCcInserted=NotificationType((1,3,6,1,4,1,629,228,100,0,134))
nbsOdsysTrapCcInserted.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:nbsOdsysTrapCcInserted.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'nbsOdsysMib':nbsOdsysMib,'nbsOdsysChasGrp':nbsOdsysChasGrp,'nbsOdsysChasTable':nbsOdsysChasTable,'nbsOdsysChasEntry':nbsOdsysChasEntry,_X:nbsOdsysChasIndex,'nbsOdsysChasCcMaxCount':nbsOdsysChasCcMaxCount,'nbsOdsysChasPsMaxCount':nbsOdsysChasPsMaxCount,'nbsOdsysChasFtMaxCount':nbsOdsysChasFtMaxCount,'nbsOdsysCcGrp':nbsOdsysCcGrp,'nbsOdsysCcTable':nbsOdsysCcTable,'nbsOdsysCcEntry':nbsOdsysCcEntry,_F:nbsOdsysCcChasIndex,_G:nbsOdsysCcBayIndex,'nbsOdsysCcChIfIndex':nbsOdsysCcChIfIndex,'nbsOdsysCcPartIndex':nbsOdsysCcPartIndex,_J:nbsOdsysCcThermActual,_K:nbsOdsysCcThermLevel,'nbsOdsysCcThermThreshLoErr':nbsOdsysCcThermThreshLoErr,'nbsOdsysCcThermThreshLoWarn':nbsOdsysCcThermThreshLoWarn,'nbsOdsysCcThermThreshHiWarn':nbsOdsysCcThermThreshHiWarn,'nbsOdsysCcThermThreshHiErr':nbsOdsysCcThermThreshHiErr,'nbsOdsysCcOperationalStatus':nbsOdsysCcOperationalStatus,'nbsOdsysFtGrp':nbsOdsysFtGrp,'nbsOdsysFtTable':nbsOdsysFtTable,'nbsOdsysFtEntry':nbsOdsysFtEntry,_H:nbsOdsysFtChasIndex,_I:nbsOdsysFtBayIndex,'nbsOdsysFtOperationalStatus':nbsOdsysFtOperationalStatus,'nbsOdsysFtChIfIndex':nbsOdsysFtChIfIndex,'nbsOdsysFtPartIndex':nbsOdsysFtPartIndex,'nbsOdsysFtFanCount':nbsOdsysFtFanCount,_L:nbsOdsysFtThermActual,_M:nbsOdsysFtThermLevel,'nbsOdsysFtThermThreshLoErr':nbsOdsysFtThermThreshLoErr,'nbsOdsysFtThermThreshLoWarn':nbsOdsysFtThermThreshLoWarn,'nbsOdsysFtThermThreshHiWarn':nbsOdsysFtThermThreshHiWarn,'nbsOdsysFtThermThreshHiErr':nbsOdsysFtThermThreshHiErr,'nbsOdsysPsGrp':nbsOdsysPsGrp,'nbsOdsysPsTable':nbsOdsysPsTable,'nbsOdsysPsEntry':nbsOdsysPsEntry,_D:nbsOdsysPsChasIndex,_E:nbsOdsysPsBayIndex,'nbsOdsysPsOperationalStatus':nbsOdsysPsOperationalStatus,'nbsOdsysPsChIfIndex':nbsOdsysPsChIfIndex,'nbsOdsysPsPartIndex':nbsOdsysPsPartIndex,'nbsOdsysPsFanCount':nbsOdsysPsFanCount,_N:nbsOdsysPsThermActual,_O:nbsOdsysPsThermLevel,'nbsOdsysPsThermThreshLoErr':nbsOdsysPsThermThreshLoErr,'nbsOdsysPsThermThreshLoWarn':nbsOdsysPsThermThreshLoWarn,'nbsOdsysPsThermThreshHiWarn':nbsOdsysPsThermThreshHiWarn,'nbsOdsysPsThermThreshHiErr':nbsOdsysPsThermThreshHiErr,_P:nbsOdsysPsVInActual,_Q:nbsOdsysPsVInLevel,'nbsOdsysPsVInThreshLoErr':nbsOdsysPsVInThreshLoErr,'nbsOdsysPsVInThreshLoWarn':nbsOdsysPsVInThreshLoWarn,'nbsOdsysPsVInThreshHiWarn':nbsOdsysPsVInThreshHiWarn,'nbsOdsysPsVInThreshHiErr':nbsOdsysPsVInThreshHiErr,_R:nbsOdsysPsVOutActual,_S:nbsOdsysPsVOutLevel,'nbsOdsysPsVOutThreshLoErr':nbsOdsysPsVOutThreshLoErr,'nbsOdsysPsVOutThreshLoWarn':nbsOdsysPsVOutThreshLoWarn,'nbsOdsysPsVOutThreshHiWarn':nbsOdsysPsVOutThreshHiWarn,'nbsOdsysPsVOutThreshHiErr':nbsOdsysPsVOutThreshHiErr,_T:nbsOdsysPsIInActual,_U:nbsOdsysPsIInLevel,'nbsOdsysPsIInThreshLoErr':nbsOdsysPsIInThreshLoErr,'nbsOdsysPsIInThreshLoWarn':nbsOdsysPsIInThreshLoWarn,'nbsOdsysPsIInThreshHiWarn':nbsOdsysPsIInThreshHiWarn,'nbsOdsysPsIInThreshHiErr':nbsOdsysPsIInThreshHiErr,_V:nbsOdsysPsIOutActual,_W:nbsOdsysPsIOutLevel,'nbsOdsysPsIOutThreshLoErr':nbsOdsysPsIOutThreshLoErr,'nbsOdsysPsIOutThreshLoWarn':nbsOdsysPsIOutThreshLoWarn,'nbsOdsysPsIOutThreshHiWarn':nbsOdsysPsIOutThreshHiWarn,'nbsOdsysPsIOutThreshHiErr':nbsOdsysPsIOutThreshHiErr,'nbsOdsysEventsGrp':nbsOdsysEventsGrp,'nbsOdsysEvents':nbsOdsysEvents,'nbsOdsysTrapCcThermLevelBad':nbsOdsysTrapCcThermLevelBad,'nbsOdsysTrapCcThermLevelOk':nbsOdsysTrapCcThermLevelOk,'nbsOdsysTrapFtThermLevelBad':nbsOdsysTrapFtThermLevelBad,'nbsOdsysTrapFtThermLevelOk':nbsOdsysTrapFtThermLevelOk,'nbsOdsysTrapPsThermLevelBad':nbsOdsysTrapPsThermLevelBad,'nbsOdsysTrapPsThermLevelOk':nbsOdsysTrapPsThermLevelOk,'nbsOdsysTrapPsVInLevelBad':nbsOdsysTrapPsVInLevelBad,'nbsOdsysTrapPsVInLevelOk':nbsOdsysTrapPsVInLevelOk,'nbsOdsysTrapPsVOutLevelBad':nbsOdsysTrapPsVOutLevelBad,'nbsOdsysTrapPsVOutLevelOk':nbsOdsysTrapPsVOutLevelOk,'nbsOdsysTrapPsIInLevelBad':nbsOdsysTrapPsIInLevelBad,'nbsOdsysTrapPsIInLevelOk':nbsOdsysTrapPsIInLevelOk,'nbsOdsysTrapPsIOutLevelBad':nbsOdsysTrapPsIOutLevelBad,'nbsOdsysTrapPsIOutLevelOk':nbsOdsysTrapPsIOutLevelOk,'nbsOdsysTrapCcFailed':nbsOdsysTrapCcFailed,'nbsOdsysTrapCcRestored':nbsOdsysTrapCcRestored,'nbsOdsysTrapCcRemoved':nbsOdsysTrapCcRemoved,'nbsOdsysTrapCcInserted':nbsOdsysTrapCcInserted})