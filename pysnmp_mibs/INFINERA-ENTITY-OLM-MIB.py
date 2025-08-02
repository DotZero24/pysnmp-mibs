_d='olmGroup'
_c='olmInstalledOTNContainerRepresentation'
_b='olmOTNContainerRepresentation'
_a='olmBwBlicensed'
_Z='olmBwBused'
_Y='olmBwBmax'
_X='olmBwQlicensed'
_W='olmBwQused'
_V='olmBwQmax'
_U='olmDefFlexLicModformat'
_T='olmRxEdfaOutputTargetPower'
_S='olmRxEdfaGain'
_R='actvTimingSource'
_Q='olmRowStatus'
_P='olmOcgNumber'
_O='olmPicDspVer'
_N='olmCurOcgNumber'
_M='olmTunableOcgNumber'
_L='olmAvailableTunableOcgNumbers'
_K='olmOperatingMode'
_J='olmProvEqptType'
_I='olmMoId'
_H='InfnOperatingMode'
_G='entLPPhysicalIndex'
_F='ENTITY-MIB'
_E='read-write'
_D='read-create'
_C='read-only'
_B='INFINERA-ENTITY-OLM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entLPPhysicalIndex,=mibBuilder.importSymbols(_F,_G)
equipment,=mibBuilder.importSymbols('INFINERA-REG-MIB','equipment')
FloatTenths,FloatThousandths,InfnAutoTunable,InfnChannelPlan,InfnEqptType,InfnOcgType,InfnOlmDefFlexLicModformat,InfnOperatingMode,InfnOtnOtuType,InfnSlteOpMode=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatTenths','FloatThousandths','InfnAutoTunable','InfnChannelPlan','InfnEqptType','InfnOcgType','InfnOlmDefFlexLicModformat',_H,'InfnOtnOtuType','InfnSlteOpMode')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
olmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,1,25))
_OlmTable_Object=MibTable
olmTable=_OlmTable_Object((1,3,6,1,4,1,21296,2,2,2,1,25,1))
if mibBuilder.loadTexts:olmTable.setStatus(_A)
_OlmEntry_Object=MibTableRow
olmEntry=_OlmEntry_Object((1,3,6,1,4,1,21296,2,2,2,1,25,1,1))
olmEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:olmEntry.setStatus(_A)
_OlmMoId_Type=DisplayString
_OlmMoId_Object=MibTableColumn
olmMoId=_OlmMoId_Object((1,3,6,1,4,1,21296,2,2,2,1,25,1,1,1),_OlmMoId_Type())
olmMoId.setMaxAccess(_D)
if mibBuilder.loadTexts:olmMoId.setStatus(_A)
_OlmProvEqptType_Type=InfnEqptType
_OlmProvEqptType_Object=MibTableColumn
olmProvEqptType=_OlmProvEqptType_Object((1,3,6,1,4,1,21296,2,2,2,1,25,1,1,2),_OlmProvEqptType_Type())
olmProvEqptType.setMaxAccess(_D)
if mibBuilder.loadTexts:olmProvEqptType.setStatus(_A)
class _OlmOperatingMode_Type(InfnOperatingMode):defaultValue=2
_OlmOperatingMode_Type.__name__=_H
_OlmOperatingMode_Object=MibTableColumn
olmOperatingMode=_OlmOperatingMode_Object((1,3,6,1,4,1,21296,2,2,2,1,25,1,1,3),_OlmOperatingMode_Type())
olmOperatingMode.setMaxAccess(_E)
if mibBuilder.loadTexts:olmOperatingMode.setStatus(_A)
_OlmAvailableTunableOcgNumbers_Type=Integer32
_OlmAvailableTunableOcgNumbers_Object=MibTableColumn
olmAvailableTunableOcgNumbers=_OlmAvailableTunableOcgNumbers_Object((1,3,6,1,4,1,21296,2,2,2,1,25,1,1,4),_OlmAvailableTunableOcgNumbers_Type())
olmAvailableTunableOcgNumbers.setMaxAccess(_C)
if mibBuilder.loadTexts:olmAvailableTunableOcgNumbers.setStatus(_A)
_OlmTunableOcgNumber_Type=Integer32
_OlmTunableOcgNumber_Object=MibTableColumn
olmTunableOcgNumber=_OlmTunableOcgNumber_Object((1,3,6,1,4,1,21296,2,2,2,1,25,1,1,5),_OlmTunableOcgNumber_Type())
olmTunableOcgNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:olmTunableOcgNumber.setStatus(_A)
_OlmCurOcgNumber_Type=Integer32
_OlmCurOcgNumber_Object=MibTableColumn
olmCurOcgNumber=_OlmCurOcgNumber_Object((1,3,6,1,4,1,21296,2,2,2,1,25,1,1,6),_OlmCurOcgNumber_Type())
olmCurOcgNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:olmCurOcgNumber.setStatus(_A)
_OlmPicDspVer_Type=DisplayString
_OlmPicDspVer_Object=MibTableColumn
olmPicDspVer=_OlmPicDspVer_Object((1,3,6,1,4,1,21296,2,2,2,1,25,1,1,7),_OlmPicDspVer_Type())
olmPicDspVer.setMaxAccess(_C)
if mibBuilder.loadTexts:olmPicDspVer.setStatus(_A)
_OlmOcgNumber_Type=Integer32
_OlmOcgNumber_Object=MibTableColumn
olmOcgNumber=_OlmOcgNumber_Object((1,3,6,1,4,1,21296,2,2,2,1,25,1,1,8),_OlmOcgNumber_Type())
olmOcgNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:olmOcgNumber.setStatus(_A)
_OlmRowStatus_Type=RowStatus
_OlmRowStatus_Object=MibTableColumn
olmRowStatus=_OlmRowStatus_Object((1,3,6,1,4,1,21296,2,2,2,1,25,1,1,9),_OlmRowStatus_Type())
olmRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:olmRowStatus.setStatus(_A)
_ActvTimingSource_Type=DisplayString
_ActvTimingSource_Object=MibTableColumn
actvTimingSource=_ActvTimingSource_Object((1,3,6,1,4,1,21296,2,2,2,1,25,1,1,10),_ActvTimingSource_Type())
actvTimingSource.setMaxAccess(_C)
if mibBuilder.loadTexts:actvTimingSource.setStatus(_A)
_OlmRxEdfaGain_Type=FloatTenths
_OlmRxEdfaGain_Object=MibTableColumn
olmRxEdfaGain=_OlmRxEdfaGain_Object((1,3,6,1,4,1,21296,2,2,2,1,25,1,1,11),_OlmRxEdfaGain_Type())
olmRxEdfaGain.setMaxAccess(_C)
if mibBuilder.loadTexts:olmRxEdfaGain.setStatus(_A)
_OlmRxEdfaOutputTargetPower_Type=FloatTenths
_OlmRxEdfaOutputTargetPower_Object=MibTableColumn
olmRxEdfaOutputTargetPower=_OlmRxEdfaOutputTargetPower_Object((1,3,6,1,4,1,21296,2,2,2,1,25,1,1,12),_OlmRxEdfaOutputTargetPower_Type())
olmRxEdfaOutputTargetPower.setMaxAccess(_C)
if mibBuilder.loadTexts:olmRxEdfaOutputTargetPower.setStatus(_A)
_OlmDefFlexLicModformat_Type=InfnOlmDefFlexLicModformat
_OlmDefFlexLicModformat_Object=MibTableColumn
olmDefFlexLicModformat=_OlmDefFlexLicModformat_Object((1,3,6,1,4,1,21296,2,2,2,1,25,1,1,13),_OlmDefFlexLicModformat_Type())
olmDefFlexLicModformat.setMaxAccess(_E)
if mibBuilder.loadTexts:olmDefFlexLicModformat.setStatus(_A)
_OlmBwQmax_Type=FloatThousandths
_OlmBwQmax_Object=MibTableColumn
olmBwQmax=_OlmBwQmax_Object((1,3,6,1,4,1,21296,2,2,2,1,25,1,1,14),_OlmBwQmax_Type())
olmBwQmax.setMaxAccess(_C)
if mibBuilder.loadTexts:olmBwQmax.setStatus(_A)
_OlmBwQused_Type=FloatThousandths
_OlmBwQused_Object=MibTableColumn
olmBwQused=_OlmBwQused_Object((1,3,6,1,4,1,21296,2,2,2,1,25,1,1,15),_OlmBwQused_Type())
olmBwQused.setMaxAccess(_C)
if mibBuilder.loadTexts:olmBwQused.setStatus(_A)
_OlmBwQlicensed_Type=FloatThousandths
_OlmBwQlicensed_Object=MibTableColumn
olmBwQlicensed=_OlmBwQlicensed_Object((1,3,6,1,4,1,21296,2,2,2,1,25,1,1,16),_OlmBwQlicensed_Type())
olmBwQlicensed.setMaxAccess(_C)
if mibBuilder.loadTexts:olmBwQlicensed.setStatus(_A)
_OlmBwBmax_Type=FloatThousandths
_OlmBwBmax_Object=MibTableColumn
olmBwBmax=_OlmBwBmax_Object((1,3,6,1,4,1,21296,2,2,2,1,25,1,1,17),_OlmBwBmax_Type())
olmBwBmax.setMaxAccess(_C)
if mibBuilder.loadTexts:olmBwBmax.setStatus(_A)
_OlmBwBused_Type=FloatThousandths
_OlmBwBused_Object=MibTableColumn
olmBwBused=_OlmBwBused_Object((1,3,6,1,4,1,21296,2,2,2,1,25,1,1,18),_OlmBwBused_Type())
olmBwBused.setMaxAccess(_C)
if mibBuilder.loadTexts:olmBwBused.setStatus(_A)
_OlmBwBlicensed_Type=FloatThousandths
_OlmBwBlicensed_Object=MibTableColumn
olmBwBlicensed=_OlmBwBlicensed_Object((1,3,6,1,4,1,21296,2,2,2,1,25,1,1,19),_OlmBwBlicensed_Type())
olmBwBlicensed.setMaxAccess(_C)
if mibBuilder.loadTexts:olmBwBlicensed.setStatus(_A)
_OlmOTNContainerRepresentation_Type=InfnOtnOtuType
_OlmOTNContainerRepresentation_Object=MibTableColumn
olmOTNContainerRepresentation=_OlmOTNContainerRepresentation_Object((1,3,6,1,4,1,21296,2,2,2,1,25,1,1,20),_OlmOTNContainerRepresentation_Type())
olmOTNContainerRepresentation.setMaxAccess(_E)
if mibBuilder.loadTexts:olmOTNContainerRepresentation.setStatus(_A)
_OlmInstalledOTNContainerRepresentation_Type=InfnOtnOtuType
_OlmInstalledOTNContainerRepresentation_Object=MibTableColumn
olmInstalledOTNContainerRepresentation=_OlmInstalledOTNContainerRepresentation_Object((1,3,6,1,4,1,21296,2,2,2,1,25,1,1,21),_OlmInstalledOTNContainerRepresentation_Type())
olmInstalledOTNContainerRepresentation.setMaxAccess(_C)
if mibBuilder.loadTexts:olmInstalledOTNContainerRepresentation.setStatus(_A)
_OlmConformance_ObjectIdentity=ObjectIdentity
olmConformance=_OlmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,25,3))
_OlmCompliances_ObjectIdentity=ObjectIdentity
olmCompliances=_OlmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,25,3,1))
_OlmGroups_ObjectIdentity=ObjectIdentity
olmGroups=_OlmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,25,3,2))
olmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,1,25,3,2,1))
olmGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:olmGroup.setStatus(_A)
olmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,1,25,3,1,1))
olmCompliance.setObjects((_B,_d))
if mibBuilder.loadTexts:olmCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'olmMIB':olmMIB,'olmTable':olmTable,'olmEntry':olmEntry,_I:olmMoId,_J:olmProvEqptType,_K:olmOperatingMode,_L:olmAvailableTunableOcgNumbers,_M:olmTunableOcgNumber,_N:olmCurOcgNumber,_O:olmPicDspVer,_P:olmOcgNumber,_Q:olmRowStatus,_R:actvTimingSource,_S:olmRxEdfaGain,_T:olmRxEdfaOutputTargetPower,_U:olmDefFlexLicModformat,_V:olmBwQmax,_W:olmBwQused,_X:olmBwQlicensed,_Y:olmBwBmax,_Z:olmBwBused,_a:olmBwBlicensed,_b:olmOTNContainerRepresentation,_c:olmInstalledOTNContainerRepresentation,'olmConformance':olmConformance,'olmCompliances':olmCompliances,'olmCompliance':olmCompliance,'olmGroups':olmGroups,_d:olmGroup})