_U='olxGroup'
_T='olxRxEdfaOutputTargetPower'
_S='olxRxEdfaGain'
_R='actvTimingSource'
_Q='olxRowStatus'
_P='olxOcgNumber'
_O='olxPicDspVer'
_N='olxCurOcgNumber'
_M='olxTunableOcgNumber'
_L='olxAvailableTunableOcgNumbers'
_K='olxOperatingMode'
_J='olxProvEqptType'
_I='olxMoId'
_H='read-write'
_G='InfnOperatingMode'
_F='entLPPhysicalIndex'
_E='ENTITY-MIB'
_D='read-create'
_C='read-only'
_B='INFINERA-ENTITY-OLX-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entLPPhysicalIndex,=mibBuilder.importSymbols(_E,_F)
equipment,=mibBuilder.importSymbols('INFINERA-REG-MIB','equipment')
InfnAutoTunable,InfnChannelPlan,InfnEqptType,InfnOcgType,InfnOperatingMode,InfnSlteOpMode=mibBuilder.importSymbols('INFINERA-TC-MIB','InfnAutoTunable','InfnChannelPlan','InfnEqptType','InfnOcgType',_G,'InfnSlteOpMode')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
olxMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,1,26))
_OlxTable_Object=MibTable
olxTable=_OlxTable_Object((1,3,6,1,4,1,21296,2,2,2,1,26,1))
if mibBuilder.loadTexts:olxTable.setStatus(_A)
_OlxEntry_Object=MibTableRow
olxEntry=_OlxEntry_Object((1,3,6,1,4,1,21296,2,2,2,1,26,1,1))
olxEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:olxEntry.setStatus(_A)
_OlxMoId_Type=DisplayString
_OlxMoId_Object=MibTableColumn
olxMoId=_OlxMoId_Object((1,3,6,1,4,1,21296,2,2,2,1,26,1,1,1),_OlxMoId_Type())
olxMoId.setMaxAccess(_D)
if mibBuilder.loadTexts:olxMoId.setStatus(_A)
_OlxProvEqptType_Type=InfnEqptType
_OlxProvEqptType_Object=MibTableColumn
olxProvEqptType=_OlxProvEqptType_Object((1,3,6,1,4,1,21296,2,2,2,1,26,1,1,2),_OlxProvEqptType_Type())
olxProvEqptType.setMaxAccess(_D)
if mibBuilder.loadTexts:olxProvEqptType.setStatus(_A)
class _OlxOperatingMode_Type(InfnOperatingMode):defaultValue=2
_OlxOperatingMode_Type.__name__=_G
_OlxOperatingMode_Object=MibTableColumn
olxOperatingMode=_OlxOperatingMode_Object((1,3,6,1,4,1,21296,2,2,2,1,26,1,1,3),_OlxOperatingMode_Type())
olxOperatingMode.setMaxAccess(_H)
if mibBuilder.loadTexts:olxOperatingMode.setStatus(_A)
_OlxAvailableTunableOcgNumbers_Type=Integer32
_OlxAvailableTunableOcgNumbers_Object=MibTableColumn
olxAvailableTunableOcgNumbers=_OlxAvailableTunableOcgNumbers_Object((1,3,6,1,4,1,21296,2,2,2,1,26,1,1,4),_OlxAvailableTunableOcgNumbers_Type())
olxAvailableTunableOcgNumbers.setMaxAccess(_C)
if mibBuilder.loadTexts:olxAvailableTunableOcgNumbers.setStatus(_A)
_OlxTunableOcgNumber_Type=Integer32
_OlxTunableOcgNumber_Object=MibTableColumn
olxTunableOcgNumber=_OlxTunableOcgNumber_Object((1,3,6,1,4,1,21296,2,2,2,1,26,1,1,5),_OlxTunableOcgNumber_Type())
olxTunableOcgNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:olxTunableOcgNumber.setStatus(_A)
_OlxCurOcgNumber_Type=Integer32
_OlxCurOcgNumber_Object=MibTableColumn
olxCurOcgNumber=_OlxCurOcgNumber_Object((1,3,6,1,4,1,21296,2,2,2,1,26,1,1,6),_OlxCurOcgNumber_Type())
olxCurOcgNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:olxCurOcgNumber.setStatus(_A)
_OlxPicDspVer_Type=DisplayString
_OlxPicDspVer_Object=MibTableColumn
olxPicDspVer=_OlxPicDspVer_Object((1,3,6,1,4,1,21296,2,2,2,1,26,1,1,7),_OlxPicDspVer_Type())
olxPicDspVer.setMaxAccess(_C)
if mibBuilder.loadTexts:olxPicDspVer.setStatus(_A)
_OlxOcgNumber_Type=Integer32
_OlxOcgNumber_Object=MibTableColumn
olxOcgNumber=_OlxOcgNumber_Object((1,3,6,1,4,1,21296,2,2,2,1,26,1,1,8),_OlxOcgNumber_Type())
olxOcgNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:olxOcgNumber.setStatus(_A)
_OlxRowStatus_Type=RowStatus
_OlxRowStatus_Object=MibTableColumn
olxRowStatus=_OlxRowStatus_Object((1,3,6,1,4,1,21296,2,2,2,1,26,1,1,9),_OlxRowStatus_Type())
olxRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:olxRowStatus.setStatus(_A)
_ActvTimingSource_Type=DisplayString
_ActvTimingSource_Object=MibTableColumn
actvTimingSource=_ActvTimingSource_Object((1,3,6,1,4,1,21296,2,2,2,1,26,1,1,10),_ActvTimingSource_Type())
actvTimingSource.setMaxAccess(_C)
if mibBuilder.loadTexts:actvTimingSource.setStatus(_A)
_OlxRxEdfaGain_Type=Integer32
_OlxRxEdfaGain_Object=MibTableColumn
olxRxEdfaGain=_OlxRxEdfaGain_Object((1,3,6,1,4,1,21296,2,2,2,1,26,1,1,11),_OlxRxEdfaGain_Type())
olxRxEdfaGain.setMaxAccess(_C)
if mibBuilder.loadTexts:olxRxEdfaGain.setStatus(_A)
_OlxRxEdfaOutputTargetPower_Type=Integer32
_OlxRxEdfaOutputTargetPower_Object=MibTableColumn
olxRxEdfaOutputTargetPower=_OlxRxEdfaOutputTargetPower_Object((1,3,6,1,4,1,21296,2,2,2,1,26,1,1,12),_OlxRxEdfaOutputTargetPower_Type())
olxRxEdfaOutputTargetPower.setMaxAccess(_C)
if mibBuilder.loadTexts:olxRxEdfaOutputTargetPower.setStatus(_A)
_OlxConformance_ObjectIdentity=ObjectIdentity
olxConformance=_OlxConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,26,3))
_OlxCompliances_ObjectIdentity=ObjectIdentity
olxCompliances=_OlxCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,26,3,1))
_OlxGroups_ObjectIdentity=ObjectIdentity
olxGroups=_OlxGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,26,3,2))
olxGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,1,26,3,2,1))
olxGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:olxGroup.setStatus(_A)
olxCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,1,26,3,1,1))
olxCompliance.setObjects((_B,_U))
if mibBuilder.loadTexts:olxCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'olxMIB':olxMIB,'olxTable':olxTable,'olxEntry':olxEntry,_I:olxMoId,_J:olxProvEqptType,_K:olxOperatingMode,_L:olxAvailableTunableOcgNumbers,_M:olxTunableOcgNumber,_N:olxCurOcgNumber,_O:olxPicDspVer,_P:olxOcgNumber,_Q:olxRowStatus,_R:actvTimingSource,_S:olxRxEdfaGain,_T:olxRxEdfaOutputTargetPower,'olxConformance':olxConformance,'olxCompliances':olxCompliances,'olxCompliance':olxCompliance,'olxGroups':olxGroups,_U:olxGroup})