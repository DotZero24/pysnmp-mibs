_Q='fmmc12Group'
_P='fmmc5Group'
_O='fmmc12OlosSoakTime'
_N='fmmc12ModelingMode'
_M='fmmc12AlienTxEDFAGain'
_L='fmmc12InputSource'
_K='fmmc12OperatingMode'
_J='fmmc12ProvEqptType'
_I='fmmc12MoId'
_H='fmmc5OperatingMode'
_G='fmmc5ProvEqptType'
_F='fmmc5MoId'
_E='entPhysicalIndex'
_D='ENTITY-MIB'
_C='read-write'
_B='INFINERA-ENTITY-FMMC-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols(_D,_E)
equipment,=mibBuilder.importSymbols('INFINERA-REG-MIB','equipment')
FloatThousandths,InfnAlienTxEDFAGain,InfnCBandOlosSoakTime,InfnEqptType,InfnModelingMode,InfnOperatingMode,InfnWaveInterfaceType=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatThousandths','InfnAlienTxEDFAGain','InfnCBandOlosSoakTime','InfnEqptType','InfnModelingMode','InfnOperatingMode','InfnWaveInterfaceType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
fmmcMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,1,47))
_Fmmc5Table_Object=MibTable
fmmc5Table=_Fmmc5Table_Object((1,3,6,1,4,1,21296,2,2,2,1,47,1))
if mibBuilder.loadTexts:fmmc5Table.setStatus(_A)
_Fmmc5Entry_Object=MibTableRow
fmmc5Entry=_Fmmc5Entry_Object((1,3,6,1,4,1,21296,2,2,2,1,47,1,1))
fmmc5Entry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:fmmc5Entry.setStatus(_A)
_Fmmc5MoId_Type=DisplayString
_Fmmc5MoId_Object=MibTableColumn
fmmc5MoId=_Fmmc5MoId_Object((1,3,6,1,4,1,21296,2,2,2,1,47,1,1,1),_Fmmc5MoId_Type())
fmmc5MoId.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmc5MoId.setStatus(_A)
_Fmmc5ProvEqptType_Type=InfnEqptType
_Fmmc5ProvEqptType_Object=MibTableColumn
fmmc5ProvEqptType=_Fmmc5ProvEqptType_Object((1,3,6,1,4,1,21296,2,2,2,1,47,1,1,2),_Fmmc5ProvEqptType_Type())
fmmc5ProvEqptType.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmc5ProvEqptType.setStatus(_A)
_Fmmc5OperatingMode_Type=InfnOperatingMode
_Fmmc5OperatingMode_Object=MibTableColumn
fmmc5OperatingMode=_Fmmc5OperatingMode_Object((1,3,6,1,4,1,21296,2,2,2,1,47,1,1,3),_Fmmc5OperatingMode_Type())
fmmc5OperatingMode.setMaxAccess('read-only')
if mibBuilder.loadTexts:fmmc5OperatingMode.setStatus(_A)
_Fmmc12Table_Object=MibTable
fmmc12Table=_Fmmc12Table_Object((1,3,6,1,4,1,21296,2,2,2,1,47,2))
if mibBuilder.loadTexts:fmmc12Table.setStatus(_A)
_Fmmc12Entry_Object=MibTableRow
fmmc12Entry=_Fmmc12Entry_Object((1,3,6,1,4,1,21296,2,2,2,1,47,2,1))
fmmc12Entry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:fmmc12Entry.setStatus(_A)
_Fmmc12MoId_Type=DisplayString
_Fmmc12MoId_Object=MibTableColumn
fmmc12MoId=_Fmmc12MoId_Object((1,3,6,1,4,1,21296,2,2,2,1,47,2,1,1),_Fmmc12MoId_Type())
fmmc12MoId.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmc12MoId.setStatus(_A)
_Fmmc12ProvEqptType_Type=InfnEqptType
_Fmmc12ProvEqptType_Object=MibTableColumn
fmmc12ProvEqptType=_Fmmc12ProvEqptType_Object((1,3,6,1,4,1,21296,2,2,2,1,47,2,1,2),_Fmmc12ProvEqptType_Type())
fmmc12ProvEqptType.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmc12ProvEqptType.setStatus(_A)
_Fmmc12OperatingMode_Type=InfnOperatingMode
_Fmmc12OperatingMode_Object=MibTableColumn
fmmc12OperatingMode=_Fmmc12OperatingMode_Object((1,3,6,1,4,1,21296,2,2,2,1,47,2,1,3),_Fmmc12OperatingMode_Type())
fmmc12OperatingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmc12OperatingMode.setStatus(_A)
_Fmmc12InputSource_Type=InfnWaveInterfaceType
_Fmmc12InputSource_Object=MibTableColumn
fmmc12InputSource=_Fmmc12InputSource_Object((1,3,6,1,4,1,21296,2,2,2,1,47,2,1,4),_Fmmc12InputSource_Type())
fmmc12InputSource.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmc12InputSource.setStatus(_A)
_Fmmc12AlienTxEDFAGain_Type=InfnAlienTxEDFAGain
_Fmmc12AlienTxEDFAGain_Object=MibTableColumn
fmmc12AlienTxEDFAGain=_Fmmc12AlienTxEDFAGain_Object((1,3,6,1,4,1,21296,2,2,2,1,47,2,1,5),_Fmmc12AlienTxEDFAGain_Type())
fmmc12AlienTxEDFAGain.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmc12AlienTxEDFAGain.setStatus(_A)
_Fmmc12ModelingMode_Type=InfnModelingMode
_Fmmc12ModelingMode_Object=MibTableColumn
fmmc12ModelingMode=_Fmmc12ModelingMode_Object((1,3,6,1,4,1,21296,2,2,2,1,47,2,1,6),_Fmmc12ModelingMode_Type())
fmmc12ModelingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmc12ModelingMode.setStatus(_A)
_Fmmc12OlosSoakTime_Type=InfnCBandOlosSoakTime
_Fmmc12OlosSoakTime_Object=MibTableColumn
fmmc12OlosSoakTime=_Fmmc12OlosSoakTime_Object((1,3,6,1,4,1,21296,2,2,2,1,47,2,1,7),_Fmmc12OlosSoakTime_Type())
fmmc12OlosSoakTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmc12OlosSoakTime.setStatus(_A)
_FmmcConformance_ObjectIdentity=ObjectIdentity
fmmcConformance=_FmmcConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,47,3))
_FmmcCompliances_ObjectIdentity=ObjectIdentity
fmmcCompliances=_FmmcCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,47,3,1))
_FmmcGroups_ObjectIdentity=ObjectIdentity
fmmcGroups=_FmmcGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,47,3,2))
fmmc5Group=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,1,47,3,2,1))
fmmc5Group.setObjects(*((_B,_F),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:fmmc5Group.setStatus(_A)
fmmc12Group=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,1,47,3,2,2))
fmmc12Group.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:fmmc12Group.setStatus(_A)
fmmcCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,1,47,3,1,1))
fmmcCompliance.setObjects((_B,_P))
if mibBuilder.loadTexts:fmmcCompliance.setStatus(_A)
fmmc12Compliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,1,47,3,1,2))
fmmc12Compliance.setObjects((_B,_Q))
if mibBuilder.loadTexts:fmmc12Compliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fmmcMIB':fmmcMIB,'fmmc5Table':fmmc5Table,'fmmc5Entry':fmmc5Entry,_F:fmmc5MoId,_G:fmmc5ProvEqptType,_H:fmmc5OperatingMode,'fmmc12Table':fmmc12Table,'fmmc12Entry':fmmc12Entry,_I:fmmc12MoId,_J:fmmc12ProvEqptType,_K:fmmc12OperatingMode,_L:fmmc12InputSource,_M:fmmc12AlienTxEDFAGain,_N:fmmc12ModelingMode,_O:fmmc12OlosSoakTime,'fmmcConformance':fmmcConformance,'fmmcCompliances':fmmcCompliances,'fmmcCompliance':fmmcCompliance,'fmmc12Compliance':fmmc12Compliance,'fmmcGroups':fmmcGroups,_P:fmmc5Group,_Q:fmmc12Group})