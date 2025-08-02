_Q='minutes'
_P='groupPduPhaseIndex'
_O='watt-hours'
_N='unresponsive'
_M='partiallyUnavailable'
_L='discovered'
_K='hostIndex'
_J='unknown'
_I='not-accessible'
_H='groupIndex'
_G='VERTIV-ONEVIEW-MIB'
_F='SnmpAdminString'
_E='watts'
_D='Integer32'
_C='Gauge32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_F)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_C,_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
vertiv=ModuleIdentity((1,3,6,1,4,1,21239))
if mibBuilder.loadTexts:vertiv.setRevisions(('2018-06-21 00:00',))
_Oneview_ObjectIdentity=ObjectIdentity
oneview=_Oneview_ObjectIdentity((1,3,6,1,4,1,21239,43))
_HostTable_Object=MibTable
hostTable=_HostTable_Object((1,3,6,1,4,1,21239,43,1))
if mibBuilder.loadTexts:hostTable.setStatus(_A)
_HostEntry_Object=MibTableRow
hostEntry=_HostEntry_Object((1,3,6,1,4,1,21239,43,1,1))
hostEntry.setIndexNames((0,_G,_K))
if mibBuilder.loadTexts:hostEntry.setStatus(_A)
class _HostIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HostIndex_Type.__name__=_D
_HostIndex_Object=MibTableColumn
hostIndex=_HostIndex_Object((1,3,6,1,4,1,21239,43,1,1,1),_HostIndex_Type())
hostIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:hostIndex.setStatus(_A)
_HostId_Type=OctetString
_HostId_Object=MibTableColumn
hostId=_HostId_Object((1,3,6,1,4,1,21239,43,1,1,2),_HostId_Type())
hostId.setMaxAccess(_B)
if mibBuilder.loadTexts:hostId.setStatus(_A)
class _HostState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('idle',1),(_L,2),(_M,3),(_N,4),(_J,5)))
_HostState_Type.__name__=_D
_HostState_Object=MibTableColumn
hostState=_HostState_Object((1,3,6,1,4,1,21239,43,1,1,3),_HostState_Type())
hostState.setMaxAccess(_B)
if mibBuilder.loadTexts:hostState.setStatus(_A)
class _HostType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('pdu',1),('environmental',2),('ups',3),('cooling',4),(_J,5)))
_HostType_Type.__name__=_D
_HostType_Object=MibTableColumn
hostType=_HostType_Object((1,3,6,1,4,1,21239,43,1,1,4),_HostType_Type())
hostType.setMaxAccess(_B)
if mibBuilder.loadTexts:hostType.setStatus(_A)
class _HostGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HostGroupIndex_Type.__name__=_D
_HostGroupIndex_Object=MibTableColumn
hostGroupIndex=_HostGroupIndex_Object((1,3,6,1,4,1,21239,43,1,1,5),_HostGroupIndex_Type())
hostGroupIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hostGroupIndex.setStatus(_A)
class _HostGroupName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,25))
_HostGroupName_Type.__name__=_F
_HostGroupName_Object=MibTableColumn
hostGroupName=_HostGroupName_Object((1,3,6,1,4,1,21239,43,1,1,6),_HostGroupName_Type())
hostGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:hostGroupName.setStatus(_A)
class _HostPortWeb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32767))
_HostPortWeb_Type.__name__=_D
_HostPortWeb_Object=MibTableColumn
hostPortWeb=_HostPortWeb_Object((1,3,6,1,4,1,21239,43,1,1,7),_HostPortWeb_Type())
hostPortWeb.setMaxAccess(_B)
if mibBuilder.loadTexts:hostPortWeb.setStatus(_A)
class _HostPortSnmp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32767))
_HostPortSnmp_Type.__name__=_D
_HostPortSnmp_Object=MibTableColumn
hostPortSnmp=_HostPortSnmp_Object((1,3,6,1,4,1,21239,43,1,1,8),_HostPortSnmp_Type())
hostPortSnmp.setMaxAccess(_B)
if mibBuilder.loadTexts:hostPortSnmp.setStatus(_A)
_Groups_ObjectIdentity=ObjectIdentity
groups=_Groups_ObjectIdentity((1,3,6,1,4,1,21239,43,2))
_GroupTable_Object=MibTable
groupTable=_GroupTable_Object((1,3,6,1,4,1,21239,43,2,1))
if mibBuilder.loadTexts:groupTable.setStatus(_A)
_GroupEntry_Object=MibTableRow
groupEntry=_GroupEntry_Object((1,3,6,1,4,1,21239,43,2,1,1))
groupEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:groupEntry.setStatus(_A)
class _GroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_GroupIndex_Type.__name__=_D
_GroupIndex_Object=MibTableColumn
groupIndex=_GroupIndex_Object((1,3,6,1,4,1,21239,43,2,1,1,1),_GroupIndex_Type())
groupIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:groupIndex.setStatus(_A)
class _GroupName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,25))
_GroupName_Type.__name__=_F
_GroupName_Object=MibTableColumn
groupName=_GroupName_Object((1,3,6,1,4,1,21239,43,2,1,1,2),_GroupName_Type())
groupName.setMaxAccess(_B)
if mibBuilder.loadTexts:groupName.setStatus(_A)
class _GroupLabel_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,25))
_GroupLabel_Type.__name__=_F
_GroupLabel_Object=MibTableColumn
groupLabel=_GroupLabel_Object((1,3,6,1,4,1,21239,43,2,1,1,3),_GroupLabel_Type())
groupLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:groupLabel.setStatus(_A)
class _GroupState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('idle',1),(_L,2),(_M,3),(_N,4),(_J,5)))
_GroupState_Type.__name__=_D
_GroupState_Object=MibTableColumn
groupState=_GroupState_Object((1,3,6,1,4,1,21239,43,2,1,1,4),_GroupState_Type())
groupState.setMaxAccess(_B)
if mibBuilder.loadTexts:groupState.setStatus(_A)
_GroupPduTotalTable_Object=MibTable
groupPduTotalTable=_GroupPduTotalTable_Object((1,3,6,1,4,1,21239,43,2,2))
if mibBuilder.loadTexts:groupPduTotalTable.setStatus(_A)
_GroupPduTotalEntry_Object=MibTableRow
groupPduTotalEntry=_GroupPduTotalEntry_Object((1,3,6,1,4,1,21239,43,2,2,1))
groupPduTotalEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:groupPduTotalEntry.setStatus(_A)
class _GroupPduTotalName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,25))
_GroupPduTotalName_Type.__name__=_F
_GroupPduTotalName_Object=MibTableColumn
groupPduTotalName=_GroupPduTotalName_Object((1,3,6,1,4,1,21239,43,2,2,1,1),_GroupPduTotalName_Type())
groupPduTotalName.setMaxAccess(_B)
if mibBuilder.loadTexts:groupPduTotalName.setStatus(_A)
class _GroupPduTotalPowerMin_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9999))
_GroupPduTotalPowerMin_Type.__name__=_C
_GroupPduTotalPowerMin_Object=MibTableColumn
groupPduTotalPowerMin=_GroupPduTotalPowerMin_Object((1,3,6,1,4,1,21239,43,2,2,1,2),_GroupPduTotalPowerMin_Type())
groupPduTotalPowerMin.setMaxAccess(_B)
if mibBuilder.loadTexts:groupPduTotalPowerMin.setStatus(_A)
if mibBuilder.loadTexts:groupPduTotalPowerMin.setUnits(_E)
class _GroupPduTotalPowerMax_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9999))
_GroupPduTotalPowerMax_Type.__name__=_C
_GroupPduTotalPowerMax_Object=MibTableColumn
groupPduTotalPowerMax=_GroupPduTotalPowerMax_Object((1,3,6,1,4,1,21239,43,2,2,1,3),_GroupPduTotalPowerMax_Type())
groupPduTotalPowerMax.setMaxAccess(_B)
if mibBuilder.loadTexts:groupPduTotalPowerMax.setStatus(_A)
if mibBuilder.loadTexts:groupPduTotalPowerMax.setUnits(_E)
class _GroupPduTotalPowerAvg_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9999))
_GroupPduTotalPowerAvg_Type.__name__=_C
_GroupPduTotalPowerAvg_Object=MibTableColumn
groupPduTotalPowerAvg=_GroupPduTotalPowerAvg_Object((1,3,6,1,4,1,21239,43,2,2,1,4),_GroupPduTotalPowerAvg_Type())
groupPduTotalPowerAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:groupPduTotalPowerAvg.setStatus(_A)
if mibBuilder.loadTexts:groupPduTotalPowerAvg.setUnits(_E)
class _GroupPduTotalPowerSum_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9999))
_GroupPduTotalPowerSum_Type.__name__=_C
_GroupPduTotalPowerSum_Object=MibTableColumn
groupPduTotalPowerSum=_GroupPduTotalPowerSum_Object((1,3,6,1,4,1,21239,43,2,2,1,5),_GroupPduTotalPowerSum_Type())
groupPduTotalPowerSum.setMaxAccess(_B)
if mibBuilder.loadTexts:groupPduTotalPowerSum.setStatus(_A)
if mibBuilder.loadTexts:groupPduTotalPowerSum.setUnits(_E)
class _GroupPduTotalEnergySum_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9999000))
_GroupPduTotalEnergySum_Type.__name__=_C
_GroupPduTotalEnergySum_Object=MibTableColumn
groupPduTotalEnergySum=_GroupPduTotalEnergySum_Object((1,3,6,1,4,1,21239,43,2,2,1,6),_GroupPduTotalEnergySum_Type())
groupPduTotalEnergySum.setMaxAccess(_B)
if mibBuilder.loadTexts:groupPduTotalEnergySum.setStatus(_A)
if mibBuilder.loadTexts:groupPduTotalEnergySum.setUnits(_O)
_GroupPduPhaseTable_Object=MibTable
groupPduPhaseTable=_GroupPduPhaseTable_Object((1,3,6,1,4,1,21239,43,2,3))
if mibBuilder.loadTexts:groupPduPhaseTable.setStatus(_A)
_GroupPduPhaseEntry_Object=MibTableRow
groupPduPhaseEntry=_GroupPduPhaseEntry_Object((1,3,6,1,4,1,21239,43,2,3,1))
groupPduPhaseEntry.setIndexNames((0,_G,_H),(0,_G,_P))
if mibBuilder.loadTexts:groupPduPhaseEntry.setStatus(_A)
class _GroupPduPhaseIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_GroupPduPhaseIndex_Type.__name__=_D
_GroupPduPhaseIndex_Object=MibTableColumn
groupPduPhaseIndex=_GroupPduPhaseIndex_Object((1,3,6,1,4,1,21239,43,2,3,1,1),_GroupPduPhaseIndex_Type())
groupPduPhaseIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:groupPduPhaseIndex.setStatus(_A)
class _GroupPduPhaseName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,25))
_GroupPduPhaseName_Type.__name__=_F
_GroupPduPhaseName_Object=MibTableColumn
groupPduPhaseName=_GroupPduPhaseName_Object((1,3,6,1,4,1,21239,43,2,3,1,2),_GroupPduPhaseName_Type())
groupPduPhaseName.setMaxAccess(_B)
if mibBuilder.loadTexts:groupPduPhaseName.setStatus(_A)
class _GroupPduPhasePowerMin_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9999))
_GroupPduPhasePowerMin_Type.__name__=_C
_GroupPduPhasePowerMin_Object=MibTableColumn
groupPduPhasePowerMin=_GroupPduPhasePowerMin_Object((1,3,6,1,4,1,21239,43,2,3,1,3),_GroupPduPhasePowerMin_Type())
groupPduPhasePowerMin.setMaxAccess(_B)
if mibBuilder.loadTexts:groupPduPhasePowerMin.setStatus(_A)
if mibBuilder.loadTexts:groupPduPhasePowerMin.setUnits(_E)
class _GroupPduPhasePowerMax_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9999))
_GroupPduPhasePowerMax_Type.__name__=_C
_GroupPduPhasePowerMax_Object=MibTableColumn
groupPduPhasePowerMax=_GroupPduPhasePowerMax_Object((1,3,6,1,4,1,21239,43,2,3,1,4),_GroupPduPhasePowerMax_Type())
groupPduPhasePowerMax.setMaxAccess(_B)
if mibBuilder.loadTexts:groupPduPhasePowerMax.setStatus(_A)
if mibBuilder.loadTexts:groupPduPhasePowerMax.setUnits(_E)
class _GroupPduPhasePowerAvg_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9999))
_GroupPduPhasePowerAvg_Type.__name__=_C
_GroupPduPhasePowerAvg_Object=MibTableColumn
groupPduPhasePowerAvg=_GroupPduPhasePowerAvg_Object((1,3,6,1,4,1,21239,43,2,3,1,5),_GroupPduPhasePowerAvg_Type())
groupPduPhasePowerAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:groupPduPhasePowerAvg.setStatus(_A)
if mibBuilder.loadTexts:groupPduPhasePowerAvg.setUnits(_E)
class _GroupPduPhasePowerSum_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9999))
_GroupPduPhasePowerSum_Type.__name__=_C
_GroupPduPhasePowerSum_Object=MibTableColumn
groupPduPhasePowerSum=_GroupPduPhasePowerSum_Object((1,3,6,1,4,1,21239,43,2,3,1,6),_GroupPduPhasePowerSum_Type())
groupPduPhasePowerSum.setMaxAccess(_B)
if mibBuilder.loadTexts:groupPduPhasePowerSum.setStatus(_A)
if mibBuilder.loadTexts:groupPduPhasePowerSum.setUnits(_E)
class _GroupPduPhaseEnergySum_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9999000))
_GroupPduPhaseEnergySum_Type.__name__=_C
_GroupPduPhaseEnergySum_Object=MibTableColumn
groupPduPhaseEnergySum=_GroupPduPhaseEnergySum_Object((1,3,6,1,4,1,21239,43,2,3,1,7),_GroupPduPhaseEnergySum_Type())
groupPduPhaseEnergySum.setMaxAccess(_B)
if mibBuilder.loadTexts:groupPduPhaseEnergySum.setStatus(_A)
if mibBuilder.loadTexts:groupPduPhaseEnergySum.setUnits(_O)
_GroupUpsTable_Object=MibTable
groupUpsTable=_GroupUpsTable_Object((1,3,6,1,4,1,21239,43,2,4))
if mibBuilder.loadTexts:groupUpsTable.setStatus(_A)
_GroupUpsEntry_Object=MibTableRow
groupUpsEntry=_GroupUpsEntry_Object((1,3,6,1,4,1,21239,43,2,4,1))
groupUpsEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:groupUpsEntry.setStatus(_A)
class _GroupUpsName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,25))
_GroupUpsName_Type.__name__=_F
_GroupUpsName_Object=MibTableColumn
groupUpsName=_GroupUpsName_Object((1,3,6,1,4,1,21239,43,2,4,1,1),_GroupUpsName_Type())
groupUpsName.setMaxAccess(_B)
if mibBuilder.loadTexts:groupUpsName.setStatus(_A)
class _GroupUpsPowerMax_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9999))
_GroupUpsPowerMax_Type.__name__=_C
_GroupUpsPowerMax_Object=MibTableColumn
groupUpsPowerMax=_GroupUpsPowerMax_Object((1,3,6,1,4,1,21239,43,2,4,1,2),_GroupUpsPowerMax_Type())
groupUpsPowerMax.setMaxAccess(_B)
if mibBuilder.loadTexts:groupUpsPowerMax.setStatus(_A)
if mibBuilder.loadTexts:groupUpsPowerMax.setUnits(_E)
class _GroupUpsPowerAvg_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9999))
_GroupUpsPowerAvg_Type.__name__=_C
_GroupUpsPowerAvg_Object=MibTableColumn
groupUpsPowerAvg=_GroupUpsPowerAvg_Object((1,3,6,1,4,1,21239,43,2,4,1,3),_GroupUpsPowerAvg_Type())
groupUpsPowerAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:groupUpsPowerAvg.setStatus(_A)
if mibBuilder.loadTexts:groupUpsPowerAvg.setUnits(_E)
class _GroupUpsBattAutonomyMin_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9999))
_GroupUpsBattAutonomyMin_Type.__name__=_C
_GroupUpsBattAutonomyMin_Object=MibTableColumn
groupUpsBattAutonomyMin=_GroupUpsBattAutonomyMin_Object((1,3,6,1,4,1,21239,43,2,4,1,4),_GroupUpsBattAutonomyMin_Type())
groupUpsBattAutonomyMin.setMaxAccess(_B)
if mibBuilder.loadTexts:groupUpsBattAutonomyMin.setStatus(_A)
if mibBuilder.loadTexts:groupUpsBattAutonomyMin.setUnits(_Q)
class _GroupUpsBattAutonomyAvg_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9999))
_GroupUpsBattAutonomyAvg_Type.__name__=_C
_GroupUpsBattAutonomyAvg_Object=MibTableColumn
groupUpsBattAutonomyAvg=_GroupUpsBattAutonomyAvg_Object((1,3,6,1,4,1,21239,43,2,4,1,5),_GroupUpsBattAutonomyAvg_Type())
groupUpsBattAutonomyAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:groupUpsBattAutonomyAvg.setStatus(_A)
if mibBuilder.loadTexts:groupUpsBattAutonomyAvg.setUnits(_Q)
class _GroupUpsBattChargeMin_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_GroupUpsBattChargeMin_Type.__name__=_C
_GroupUpsBattChargeMin_Object=MibTableColumn
groupUpsBattChargeMin=_GroupUpsBattChargeMin_Object((1,3,6,1,4,1,21239,43,2,4,1,6),_GroupUpsBattChargeMin_Type())
groupUpsBattChargeMin.setMaxAccess(_B)
if mibBuilder.loadTexts:groupUpsBattChargeMin.setStatus(_A)
if mibBuilder.loadTexts:groupUpsBattChargeMin.setUnits('%')
class _GroupUpsBattChargeAvg_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_GroupUpsBattChargeAvg_Type.__name__=_C
_GroupUpsBattChargeAvg_Object=MibTableColumn
groupUpsBattChargeAvg=_GroupUpsBattChargeAvg_Object((1,3,6,1,4,1,21239,43,2,4,1,7),_GroupUpsBattChargeAvg_Type())
groupUpsBattChargeAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:groupUpsBattChargeAvg.setStatus(_A)
if mibBuilder.loadTexts:groupUpsBattChargeAvg.setUnits('%')
_GroupEnvTable_Object=MibTable
groupEnvTable=_GroupEnvTable_Object((1,3,6,1,4,1,21239,43,2,5))
if mibBuilder.loadTexts:groupEnvTable.setStatus(_A)
_GroupEnvEntry_Object=MibTableRow
groupEnvEntry=_GroupEnvEntry_Object((1,3,6,1,4,1,21239,43,2,5,1))
groupEnvEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:groupEnvEntry.setStatus(_A)
class _GroupEnvName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,25))
_GroupEnvName_Type.__name__=_F
_GroupEnvName_Object=MibTableColumn
groupEnvName=_GroupEnvName_Object((1,3,6,1,4,1,21239,43,2,5,1,1),_GroupEnvName_Type())
groupEnvName.setMaxAccess(_B)
if mibBuilder.loadTexts:groupEnvName.setStatus(_A)
class _GroupEnvTempMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-400,2540))
_GroupEnvTempMin_Type.__name__=_D
_GroupEnvTempMin_Object=MibTableColumn
groupEnvTempMin=_GroupEnvTempMin_Object((1,3,6,1,4,1,21239,43,2,5,1,2),_GroupEnvTempMin_Type())
groupEnvTempMin.setMaxAccess(_B)
if mibBuilder.loadTexts:groupEnvTempMin.setStatus(_A)
class _GroupEnvTempMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-400,2540))
_GroupEnvTempMax_Type.__name__=_D
_GroupEnvTempMax_Object=MibTableColumn
groupEnvTempMax=_GroupEnvTempMax_Object((1,3,6,1,4,1,21239,43,2,5,1,3),_GroupEnvTempMax_Type())
groupEnvTempMax.setMaxAccess(_B)
if mibBuilder.loadTexts:groupEnvTempMax.setStatus(_A)
class _GroupEnvTempAvg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-400,2540))
_GroupEnvTempAvg_Type.__name__=_D
_GroupEnvTempAvg_Object=MibTableColumn
groupEnvTempAvg=_GroupEnvTempAvg_Object((1,3,6,1,4,1,21239,43,2,5,1,4),_GroupEnvTempAvg_Type())
groupEnvTempAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:groupEnvTempAvg.setStatus(_A)
class _GroupEnvHumidityMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_GroupEnvHumidityMin_Type.__name__=_D
_GroupEnvHumidityMin_Object=MibTableColumn
groupEnvHumidityMin=_GroupEnvHumidityMin_Object((1,3,6,1,4,1,21239,43,2,5,1,5),_GroupEnvHumidityMin_Type())
groupEnvHumidityMin.setMaxAccess(_B)
if mibBuilder.loadTexts:groupEnvHumidityMin.setStatus(_A)
if mibBuilder.loadTexts:groupEnvHumidityMin.setUnits('%')
class _GroupEnvHumidityMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_GroupEnvHumidityMax_Type.__name__=_D
_GroupEnvHumidityMax_Object=MibTableColumn
groupEnvHumidityMax=_GroupEnvHumidityMax_Object((1,3,6,1,4,1,21239,43,2,5,1,6),_GroupEnvHumidityMax_Type())
groupEnvHumidityMax.setMaxAccess(_B)
if mibBuilder.loadTexts:groupEnvHumidityMax.setStatus(_A)
if mibBuilder.loadTexts:groupEnvHumidityMax.setUnits('%')
class _GroupEnvHumidityAvg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_GroupEnvHumidityAvg_Type.__name__=_D
_GroupEnvHumidityAvg_Object=MibTableColumn
groupEnvHumidityAvg=_GroupEnvHumidityAvg_Object((1,3,6,1,4,1,21239,43,2,5,1,7),_GroupEnvHumidityAvg_Type())
groupEnvHumidityAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:groupEnvHumidityAvg.setStatus(_A)
if mibBuilder.loadTexts:groupEnvHumidityAvg.setUnits('%')
mibBuilder.exportSymbols(_G,**{'vertiv':vertiv,'oneview':oneview,'hostTable':hostTable,'hostEntry':hostEntry,_K:hostIndex,'hostId':hostId,'hostState':hostState,'hostType':hostType,'hostGroupIndex':hostGroupIndex,'hostGroupName':hostGroupName,'hostPortWeb':hostPortWeb,'hostPortSnmp':hostPortSnmp,'groups':groups,'groupTable':groupTable,'groupEntry':groupEntry,_H:groupIndex,'groupName':groupName,'groupLabel':groupLabel,'groupState':groupState,'groupPduTotalTable':groupPduTotalTable,'groupPduTotalEntry':groupPduTotalEntry,'groupPduTotalName':groupPduTotalName,'groupPduTotalPowerMin':groupPduTotalPowerMin,'groupPduTotalPowerMax':groupPduTotalPowerMax,'groupPduTotalPowerAvg':groupPduTotalPowerAvg,'groupPduTotalPowerSum':groupPduTotalPowerSum,'groupPduTotalEnergySum':groupPduTotalEnergySum,'groupPduPhaseTable':groupPduPhaseTable,'groupPduPhaseEntry':groupPduPhaseEntry,_P:groupPduPhaseIndex,'groupPduPhaseName':groupPduPhaseName,'groupPduPhasePowerMin':groupPduPhasePowerMin,'groupPduPhasePowerMax':groupPduPhasePowerMax,'groupPduPhasePowerAvg':groupPduPhasePowerAvg,'groupPduPhasePowerSum':groupPduPhasePowerSum,'groupPduPhaseEnergySum':groupPduPhaseEnergySum,'groupUpsTable':groupUpsTable,'groupUpsEntry':groupUpsEntry,'groupUpsName':groupUpsName,'groupUpsPowerMax':groupUpsPowerMax,'groupUpsPowerAvg':groupUpsPowerAvg,'groupUpsBattAutonomyMin':groupUpsBattAutonomyMin,'groupUpsBattAutonomyAvg':groupUpsBattAutonomyAvg,'groupUpsBattChargeMin':groupUpsBattChargeMin,'groupUpsBattChargeAvg':groupUpsBattChargeAvg,'groupEnvTable':groupEnvTable,'groupEnvEntry':groupEnvEntry,'groupEnvName':groupEnvName,'groupEnvTempMin':groupEnvTempMin,'groupEnvTempMax':groupEnvTempMax,'groupEnvTempAvg':groupEnvTempAvg,'groupEnvHumidityMin':groupEnvHumidityMin,'groupEnvHumidityMax':groupEnvHumidityMax,'groupEnvHumidityAvg':groupEnvHumidityAvg})