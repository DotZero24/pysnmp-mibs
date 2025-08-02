_R='arubaWiredSystemInfoTableGroup'
_Q='arubaWiredSystemInfoCpuAvgFiveMin'
_P='arubaWiredSystemInfoCpuAvgOneMin'
_O='arubaWiredSystemInfoStorageSelftest'
_N='arubaWiredSystemInfoStorageSecurity'
_M='arubaWiredSystemInfoStorageCoredump'
_L='arubaWiredSystemInfoStorageLog'
_K='arubaWiredSystemInfoStorageNos'
_J='arubaWiredSystemInfoMemory'
_I='arubaWiredSystemInfoCpu'
_H='not-accessible'
_G='arubaWiredSystemInfoModuleName'
_F='arubaWiredSystemInfoModuleType'
_E='DisplayString'
_D='read-only'
_C='Unsigned32'
_B='ARUBAWIRED-SYSTEMINFO-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
wndFeatures,=mibBuilder.importSymbols('ARUBAWIRED-NETWORKING-OID','wndFeatures')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
arubaWiredSystemInfoMIB=ModuleIdentity((1,3,6,1,4,1,47196,4,1,1,3,22))
if mibBuilder.loadTexts:arubaWiredSystemInfoMIB.setRevisions(('2021-11-08 00:00',))
_ArubaWiredSystemInfoNotifications_ObjectIdentity=ObjectIdentity
arubaWiredSystemInfoNotifications=_ArubaWiredSystemInfoNotifications_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,22,0))
_ArubaWiredSystemInfoObjects_ObjectIdentity=ObjectIdentity
arubaWiredSystemInfoObjects=_ArubaWiredSystemInfoObjects_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,22,1))
_ArubaWiredSystemInfo_ObjectIdentity=ObjectIdentity
arubaWiredSystemInfo=_ArubaWiredSystemInfo_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,22,1,0))
_ArubaWiredSystemInfoTable_Object=MibTable
arubaWiredSystemInfoTable=_ArubaWiredSystemInfoTable_Object((1,3,6,1,4,1,47196,4,1,1,3,22,1,0,1))
if mibBuilder.loadTexts:arubaWiredSystemInfoTable.setStatus(_A)
_ArubaWiredSystemInfoEntry_Object=MibTableRow
arubaWiredSystemInfoEntry=_ArubaWiredSystemInfoEntry_Object((1,3,6,1,4,1,47196,4,1,1,3,22,1,0,1,1))
arubaWiredSystemInfoEntry.setIndexNames((0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:arubaWiredSystemInfoEntry.setStatus(_A)
class _ArubaWiredSystemInfoModuleType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_ArubaWiredSystemInfoModuleType_Type.__name__=_E
_ArubaWiredSystemInfoModuleType_Object=MibTableColumn
arubaWiredSystemInfoModuleType=_ArubaWiredSystemInfoModuleType_Object((1,3,6,1,4,1,47196,4,1,1,3,22,1,0,1,1,1),_ArubaWiredSystemInfoModuleType_Type())
arubaWiredSystemInfoModuleType.setMaxAccess(_H)
if mibBuilder.loadTexts:arubaWiredSystemInfoModuleType.setStatus(_A)
class _ArubaWiredSystemInfoModuleName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_ArubaWiredSystemInfoModuleName_Type.__name__=_E
_ArubaWiredSystemInfoModuleName_Object=MibTableColumn
arubaWiredSystemInfoModuleName=_ArubaWiredSystemInfoModuleName_Object((1,3,6,1,4,1,47196,4,1,1,3,22,1,0,1,1,2),_ArubaWiredSystemInfoModuleName_Type())
arubaWiredSystemInfoModuleName.setMaxAccess(_H)
if mibBuilder.loadTexts:arubaWiredSystemInfoModuleName.setStatus(_A)
class _ArubaWiredSystemInfoCpu_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ArubaWiredSystemInfoCpu_Type.__name__=_C
_ArubaWiredSystemInfoCpu_Object=MibTableColumn
arubaWiredSystemInfoCpu=_ArubaWiredSystemInfoCpu_Object((1,3,6,1,4,1,47196,4,1,1,3,22,1,0,1,1,3),_ArubaWiredSystemInfoCpu_Type())
arubaWiredSystemInfoCpu.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredSystemInfoCpu.setStatus(_A)
class _ArubaWiredSystemInfoMemory_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ArubaWiredSystemInfoMemory_Type.__name__=_C
_ArubaWiredSystemInfoMemory_Object=MibTableColumn
arubaWiredSystemInfoMemory=_ArubaWiredSystemInfoMemory_Object((1,3,6,1,4,1,47196,4,1,1,3,22,1,0,1,1,4),_ArubaWiredSystemInfoMemory_Type())
arubaWiredSystemInfoMemory.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredSystemInfoMemory.setStatus(_A)
class _ArubaWiredSystemInfoStorageNos_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ArubaWiredSystemInfoStorageNos_Type.__name__=_C
_ArubaWiredSystemInfoStorageNos_Object=MibTableColumn
arubaWiredSystemInfoStorageNos=_ArubaWiredSystemInfoStorageNos_Object((1,3,6,1,4,1,47196,4,1,1,3,22,1,0,1,1,5),_ArubaWiredSystemInfoStorageNos_Type())
arubaWiredSystemInfoStorageNos.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredSystemInfoStorageNos.setStatus(_A)
class _ArubaWiredSystemInfoStorageLog_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ArubaWiredSystemInfoStorageLog_Type.__name__=_C
_ArubaWiredSystemInfoStorageLog_Object=MibTableColumn
arubaWiredSystemInfoStorageLog=_ArubaWiredSystemInfoStorageLog_Object((1,3,6,1,4,1,47196,4,1,1,3,22,1,0,1,1,6),_ArubaWiredSystemInfoStorageLog_Type())
arubaWiredSystemInfoStorageLog.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredSystemInfoStorageLog.setStatus(_A)
class _ArubaWiredSystemInfoStorageCoredump_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ArubaWiredSystemInfoStorageCoredump_Type.__name__=_C
_ArubaWiredSystemInfoStorageCoredump_Object=MibTableColumn
arubaWiredSystemInfoStorageCoredump=_ArubaWiredSystemInfoStorageCoredump_Object((1,3,6,1,4,1,47196,4,1,1,3,22,1,0,1,1,7),_ArubaWiredSystemInfoStorageCoredump_Type())
arubaWiredSystemInfoStorageCoredump.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredSystemInfoStorageCoredump.setStatus(_A)
class _ArubaWiredSystemInfoStorageSecurity_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ArubaWiredSystemInfoStorageSecurity_Type.__name__=_C
_ArubaWiredSystemInfoStorageSecurity_Object=MibTableColumn
arubaWiredSystemInfoStorageSecurity=_ArubaWiredSystemInfoStorageSecurity_Object((1,3,6,1,4,1,47196,4,1,1,3,22,1,0,1,1,8),_ArubaWiredSystemInfoStorageSecurity_Type())
arubaWiredSystemInfoStorageSecurity.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredSystemInfoStorageSecurity.setStatus(_A)
class _ArubaWiredSystemInfoStorageSelftest_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ArubaWiredSystemInfoStorageSelftest_Type.__name__=_C
_ArubaWiredSystemInfoStorageSelftest_Object=MibTableColumn
arubaWiredSystemInfoStorageSelftest=_ArubaWiredSystemInfoStorageSelftest_Object((1,3,6,1,4,1,47196,4,1,1,3,22,1,0,1,1,9),_ArubaWiredSystemInfoStorageSelftest_Type())
arubaWiredSystemInfoStorageSelftest.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredSystemInfoStorageSelftest.setStatus(_A)
class _ArubaWiredSystemInfoCpuAvgOneMin_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ArubaWiredSystemInfoCpuAvgOneMin_Type.__name__=_C
_ArubaWiredSystemInfoCpuAvgOneMin_Object=MibTableColumn
arubaWiredSystemInfoCpuAvgOneMin=_ArubaWiredSystemInfoCpuAvgOneMin_Object((1,3,6,1,4,1,47196,4,1,1,3,22,1,0,1,1,10),_ArubaWiredSystemInfoCpuAvgOneMin_Type())
arubaWiredSystemInfoCpuAvgOneMin.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredSystemInfoCpuAvgOneMin.setStatus(_A)
class _ArubaWiredSystemInfoCpuAvgFiveMin_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ArubaWiredSystemInfoCpuAvgFiveMin_Type.__name__=_C
_ArubaWiredSystemInfoCpuAvgFiveMin_Object=MibTableColumn
arubaWiredSystemInfoCpuAvgFiveMin=_ArubaWiredSystemInfoCpuAvgFiveMin_Object((1,3,6,1,4,1,47196,4,1,1,3,22,1,0,1,1,11),_ArubaWiredSystemInfoCpuAvgFiveMin_Type())
arubaWiredSystemInfoCpuAvgFiveMin.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredSystemInfoCpuAvgFiveMin.setStatus(_A)
_ArubaWiredSystemInfoConformance_ObjectIdentity=ObjectIdentity
arubaWiredSystemInfoConformance=_ArubaWiredSystemInfoConformance_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,22,2))
_ArubaWiredSystemInfoCompliances_ObjectIdentity=ObjectIdentity
arubaWiredSystemInfoCompliances=_ArubaWiredSystemInfoCompliances_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,22,2,1))
_ArubaWiredSystemInfoGroups_ObjectIdentity=ObjectIdentity
arubaWiredSystemInfoGroups=_ArubaWiredSystemInfoGroups_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,22,2,2))
arubaWiredSystemInfoTableGroup=ObjectGroup((1,3,6,1,4,1,47196,4,1,1,3,22,2,2,1))
arubaWiredSystemInfoTableGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:arubaWiredSystemInfoTableGroup.setStatus(_A)
arubaWiredSystemInfoCompliance=ModuleCompliance((1,3,6,1,4,1,47196,4,1,1,3,22,2,1,1))
arubaWiredSystemInfoCompliance.setObjects((_B,_R))
if mibBuilder.loadTexts:arubaWiredSystemInfoCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'arubaWiredSystemInfoMIB':arubaWiredSystemInfoMIB,'arubaWiredSystemInfoNotifications':arubaWiredSystemInfoNotifications,'arubaWiredSystemInfoObjects':arubaWiredSystemInfoObjects,'arubaWiredSystemInfo':arubaWiredSystemInfo,'arubaWiredSystemInfoTable':arubaWiredSystemInfoTable,'arubaWiredSystemInfoEntry':arubaWiredSystemInfoEntry,_F:arubaWiredSystemInfoModuleType,_G:arubaWiredSystemInfoModuleName,_I:arubaWiredSystemInfoCpu,_J:arubaWiredSystemInfoMemory,_K:arubaWiredSystemInfoStorageNos,_L:arubaWiredSystemInfoStorageLog,_M:arubaWiredSystemInfoStorageCoredump,_N:arubaWiredSystemInfoStorageSecurity,_O:arubaWiredSystemInfoStorageSelftest,_P:arubaWiredSystemInfoCpuAvgOneMin,_Q:arubaWiredSystemInfoCpuAvgFiveMin,'arubaWiredSystemInfoConformance':arubaWiredSystemInfoConformance,'arubaWiredSystemInfoCompliances':arubaWiredSystemInfoCompliances,'arubaWiredSystemInfoCompliance':arubaWiredSystemInfoCompliance,'arubaWiredSystemInfoGroups':arubaWiredSystemInfoGroups,_R:arubaWiredSystemInfoTableGroup})