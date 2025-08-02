_d='picaConfigGroup'
_c='picarpsuGroup'
_b='picasfpGroup'
_a='picaBasicGroup'
_Z='tftpBatchFilePath'
_Y='tftpConfigFilePath'
_X='rpsuStatus'
_W='sfpType'
_V='sfpRxPower'
_U='sfpTxPower'
_T='sfpBias'
_S='sfpVoltage'
_R='sfpTemp'
_Q='sfpSerialNumber'
_P='sfpVendorName'
_O='switchChipTemperature'
_N='cpuTemperature'
_M='switchTemperature'
_L='freePhyMemory'
_K='usedPhyMemory'
_J='totalPhyMemory'
_I='cpuUsage'
_H='read-write'
_G='rpsuIndex'
_F='sfpIndex'
_E='OctetString'
_D='Integer32'
_C='read-only'
_B='PICA-PRIVATE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
IANAifType,=mibBuilder.importSymbols('IANAifType-MIB','IANAifType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
snmpTraps,=mibBuilder.importSymbols('SNMPv2-MIB','snmpTraps')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso,mib_2,snmpModules=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso','mib-2','snmpModules')
AutonomousType,DisplayString,PhysAddress,RowStatus,TextualConvention,TestAndIncr,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','AutonomousType','DisplayString','PhysAddress','RowStatus','TextualConvention','TestAndIncr','TimeStamp','TruthValue')
picaPrivateMib=ModuleIdentity((1,3,6,1,4,1,35098))
if mibBuilder.loadTexts:picaPrivateMib.setRevisions(('2011-04-28 00:00',))
_HostStatusGroup_ObjectIdentity=ObjectIdentity
hostStatusGroup=_HostStatusGroup_ObjectIdentity((1,3,6,1,4,1,35098,1))
class _CpuUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CpuUsage_Type.__name__=_D
_CpuUsage_Object=MibScalar
cpuUsage=_CpuUsage_Object((1,3,6,1,4,1,35098,1,1),_CpuUsage_Type())
cpuUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:cpuUsage.setStatus(_A)
_TotalPhyMemory_Type=DisplayString
_TotalPhyMemory_Object=MibScalar
totalPhyMemory=_TotalPhyMemory_Object((1,3,6,1,4,1,35098,1,2),_TotalPhyMemory_Type())
totalPhyMemory.setMaxAccess(_C)
if mibBuilder.loadTexts:totalPhyMemory.setStatus(_A)
_UsedPhyMemory_Type=DisplayString
_UsedPhyMemory_Object=MibScalar
usedPhyMemory=_UsedPhyMemory_Object((1,3,6,1,4,1,35098,1,3),_UsedPhyMemory_Type())
usedPhyMemory.setMaxAccess(_C)
if mibBuilder.loadTexts:usedPhyMemory.setStatus(_A)
_FreePhyMemory_Type=DisplayString
_FreePhyMemory_Object=MibScalar
freePhyMemory=_FreePhyMemory_Object((1,3,6,1,4,1,35098,1,4),_FreePhyMemory_Type())
freePhyMemory.setMaxAccess(_C)
if mibBuilder.loadTexts:freePhyMemory.setStatus(_A)
class _SwitchTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,500))
_SwitchTemperature_Type.__name__=_D
_SwitchTemperature_Object=MibScalar
switchTemperature=_SwitchTemperature_Object((1,3,6,1,4,1,35098,1,5),_SwitchTemperature_Type())
switchTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:switchTemperature.setStatus(_A)
class _CpuTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,500))
_CpuTemperature_Type.__name__=_D
_CpuTemperature_Object=MibScalar
cpuTemperature=_CpuTemperature_Object((1,3,6,1,4,1,35098,1,6),_CpuTemperature_Type())
cpuTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:cpuTemperature.setStatus(_A)
class _SwitchChipTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,500))
_SwitchChipTemperature_Type.__name__=_D
_SwitchChipTemperature_Object=MibScalar
switchChipTemperature=_SwitchChipTemperature_Object((1,3,6,1,4,1,35098,1,7),_SwitchChipTemperature_Type())
switchChipTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:switchChipTemperature.setStatus(_A)
_SfpstatusTable_Object=MibTable
sfpstatusTable=_SfpstatusTable_Object((1,3,6,1,4,1,35098,1,8))
if mibBuilder.loadTexts:sfpstatusTable.setStatus(_A)
_SfpstatusEntry_Object=MibTableRow
sfpstatusEntry=_SfpstatusEntry_Object((1,3,6,1,4,1,35098,1,8,1))
sfpstatusEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:sfpstatusEntry.setStatus(_A)
class _SfpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SfpIndex_Type.__name__=_D
_SfpIndex_Object=MibTableColumn
sfpIndex=_SfpIndex_Object((1,3,6,1,4,1,35098,1,8,1,1),_SfpIndex_Type())
sfpIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpIndex.setStatus(_A)
_SfpVendorName_Type=DisplayString
_SfpVendorName_Object=MibTableColumn
sfpVendorName=_SfpVendorName_Object((1,3,6,1,4,1,35098,1,8,1,2),_SfpVendorName_Type())
sfpVendorName.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpVendorName.setStatus(_A)
_SfpSerialNumber_Type=DisplayString
_SfpSerialNumber_Object=MibTableColumn
sfpSerialNumber=_SfpSerialNumber_Object((1,3,6,1,4,1,35098,1,8,1,3),_SfpSerialNumber_Type())
sfpSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpSerialNumber.setStatus(_A)
_SfpTemp_Type=Integer32
_SfpTemp_Object=MibTableColumn
sfpTemp=_SfpTemp_Object((1,3,6,1,4,1,35098,1,8,1,4),_SfpTemp_Type())
sfpTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpTemp.setStatus(_A)
_SfpVoltage_Type=Integer32
_SfpVoltage_Object=MibTableColumn
sfpVoltage=_SfpVoltage_Object((1,3,6,1,4,1,35098,1,8,1,5),_SfpVoltage_Type())
sfpVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpVoltage.setStatus(_A)
_SfpBias_Type=Integer32
_SfpBias_Object=MibTableColumn
sfpBias=_SfpBias_Object((1,3,6,1,4,1,35098,1,8,1,6),_SfpBias_Type())
sfpBias.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpBias.setStatus(_A)
_SfpTxPower_Type=Integer32
_SfpTxPower_Object=MibTableColumn
sfpTxPower=_SfpTxPower_Object((1,3,6,1,4,1,35098,1,8,1,7),_SfpTxPower_Type())
sfpTxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpTxPower.setStatus(_A)
_SfpRxPower_Type=Integer32
_SfpRxPower_Object=MibTableColumn
sfpRxPower=_SfpRxPower_Object((1,3,6,1,4,1,35098,1,8,1,8),_SfpRxPower_Type())
sfpRxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpRxPower.setStatus(_A)
_SfpType_Type=DisplayString
_SfpType_Object=MibTableColumn
sfpType=_SfpType_Object((1,3,6,1,4,1,35098,1,8,1,9),_SfpType_Type())
sfpType.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpType.setStatus(_A)
_RpsustatusTable_Object=MibTable
rpsustatusTable=_RpsustatusTable_Object((1,3,6,1,4,1,35098,1,9))
if mibBuilder.loadTexts:rpsustatusTable.setStatus(_A)
_RpsustatusEntry_Object=MibTableRow
rpsustatusEntry=_RpsustatusEntry_Object((1,3,6,1,4,1,35098,1,9,1))
rpsustatusEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:rpsustatusEntry.setStatus(_A)
class _RpsuIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RpsuIndex_Type.__name__=_D
_RpsuIndex_Object=MibTableColumn
rpsuIndex=_RpsuIndex_Object((1,3,6,1,4,1,35098,1,9,1,1),_RpsuIndex_Type())
rpsuIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rpsuIndex.setStatus(_A)
class _RpsuStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_RpsuStatus_Type.__name__=_D
_RpsuStatus_Object=MibTableColumn
rpsuStatus=_RpsuStatus_Object((1,3,6,1,4,1,35098,1,9,1,2),_RpsuStatus_Type())
rpsuStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rpsuStatus.setStatus(_A)
_SwitchConfigGroup_ObjectIdentity=ObjectIdentity
switchConfigGroup=_SwitchConfigGroup_ObjectIdentity((1,3,6,1,4,1,35098,2))
class _TftpConfigFilePath_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,255))
_TftpConfigFilePath_Type.__name__=_E
_TftpConfigFilePath_Object=MibScalar
tftpConfigFilePath=_TftpConfigFilePath_Object((1,3,6,1,4,1,35098,2,0),_TftpConfigFilePath_Type())
tftpConfigFilePath.setMaxAccess(_H)
if mibBuilder.loadTexts:tftpConfigFilePath.setStatus(_A)
class _TftpBatchFilePath_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,255))
_TftpBatchFilePath_Type.__name__=_E
_TftpBatchFilePath_Object=MibScalar
tftpBatchFilePath=_TftpBatchFilePath_Object((1,3,6,1,4,1,35098,2,1),_TftpBatchFilePath_Type())
tftpBatchFilePath.setMaxAccess(_H)
if mibBuilder.loadTexts:tftpBatchFilePath.setStatus(_A)
_PicaConformance_ObjectIdentity=ObjectIdentity
picaConformance=_PicaConformance_ObjectIdentity((1,3,6,1,4,1,35098,20))
_PicaGroups_ObjectIdentity=ObjectIdentity
picaGroups=_PicaGroups_ObjectIdentity((1,3,6,1,4,1,35098,20,1))
_PicaCompliances_ObjectIdentity=ObjectIdentity
picaCompliances=_PicaCompliances_ObjectIdentity((1,3,6,1,4,1,35098,20,2))
picaBasicGroup=ObjectGroup((1,3,6,1,4,1,35098,20,1,1))
picaBasicGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:picaBasicGroup.setStatus(_A)
picasfpGroup=ObjectGroup((1,3,6,1,4,1,35098,20,1,2))
picasfpGroup.setObjects(*((_B,_F),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:picasfpGroup.setStatus(_A)
picarpsuGroup=ObjectGroup((1,3,6,1,4,1,35098,20,1,3))
picarpsuGroup.setObjects(*((_B,_G),(_B,_X)))
if mibBuilder.loadTexts:picarpsuGroup.setStatus(_A)
picaConfigGroup=ObjectGroup((1,3,6,1,4,1,35098,20,1,4))
picaConfigGroup.setObjects(*((_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:picaConfigGroup.setStatus(_A)
picaCompliance=ModuleCompliance((1,3,6,1,4,1,35098,20,2,1))
picaCompliance.setObjects(*((_B,_a),(_B,_b),(_B,_c),(_B,_d)))
if mibBuilder.loadTexts:picaCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'picaPrivateMib':picaPrivateMib,'hostStatusGroup':hostStatusGroup,_I:cpuUsage,_J:totalPhyMemory,_K:usedPhyMemory,_L:freePhyMemory,_M:switchTemperature,_N:cpuTemperature,_O:switchChipTemperature,'sfpstatusTable':sfpstatusTable,'sfpstatusEntry':sfpstatusEntry,_F:sfpIndex,_P:sfpVendorName,_Q:sfpSerialNumber,_R:sfpTemp,_S:sfpVoltage,_T:sfpBias,_U:sfpTxPower,_V:sfpRxPower,_W:sfpType,'rpsustatusTable':rpsustatusTable,'rpsustatusEntry':rpsustatusEntry,_G:rpsuIndex,_X:rpsuStatus,'switchConfigGroup':switchConfigGroup,_Y:tftpConfigFilePath,_Z:tftpBatchFilePath,'picaConformance':picaConformance,'picaGroups':picaGroups,_a:picaBasicGroup,_b:picasfpGroup,_c:picarpsuGroup,_d:picaConfigGroup,'picaCompliances':picaCompliances,'picaCompliance':picaCompliance})