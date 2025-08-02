_G='systemFLASHutilizationUnitID'
_F='systemDRAMutilizationUnitID'
_E='DGS-6600-SYSTEM-INFO-MIB'
_D='Integer32'
_C='KB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dgs6600_system,=mibBuilder.importSymbols('DGS-6600-ID-MIB','dgs6600-system')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
dgs6600SystemInfoMIB=ModuleIdentity((1,3,6,1,4,1,171,10,120,100,1,1))
_SystemBasicInfo_ObjectIdentity=ObjectIdentity
systemBasicInfo=_SystemBasicInfo_ObjectIdentity((1,3,6,1,4,1,171,10,120,100,1,1,1))
_SystemCPUutilization_ObjectIdentity=ObjectIdentity
systemCPUutilization=_SystemCPUutilization_ObjectIdentity((1,3,6,1,4,1,171,10,120,100,1,1,1,1))
_SystemCPUutilizationIn5sec_Type=Integer32
_SystemCPUutilizationIn5sec_Object=MibScalar
systemCPUutilizationIn5sec=_SystemCPUutilizationIn5sec_Object((1,3,6,1,4,1,171,10,120,100,1,1,1,1,1),_SystemCPUutilizationIn5sec_Type())
systemCPUutilizationIn5sec.setMaxAccess(_B)
if mibBuilder.loadTexts:systemCPUutilizationIn5sec.setStatus(_A)
_SystemCPUutilizationIn1min_Type=Integer32
_SystemCPUutilizationIn1min_Object=MibScalar
systemCPUutilizationIn1min=_SystemCPUutilizationIn1min_Object((1,3,6,1,4,1,171,10,120,100,1,1,1,1,2),_SystemCPUutilizationIn1min_Type())
systemCPUutilizationIn1min.setMaxAccess(_B)
if mibBuilder.loadTexts:systemCPUutilizationIn1min.setStatus(_A)
_SystemCPUutilizationIn5min_Type=Integer32
_SystemCPUutilizationIn5min_Object=MibScalar
systemCPUutilizationIn5min=_SystemCPUutilizationIn5min_Object((1,3,6,1,4,1,171,10,120,100,1,1,1,1,3),_SystemCPUutilizationIn5min_Type())
systemCPUutilizationIn5min.setMaxAccess(_B)
if mibBuilder.loadTexts:systemCPUutilizationIn5min.setStatus(_A)
_SystemDRAMutilizationTable_Object=MibTable
systemDRAMutilizationTable=_SystemDRAMutilizationTable_Object((1,3,6,1,4,1,171,10,120,100,1,1,1,2))
if mibBuilder.loadTexts:systemDRAMutilizationTable.setStatus(_A)
_SystemDRAMutilizationEntry_Object=MibTableRow
systemDRAMutilizationEntry=_SystemDRAMutilizationEntry_Object((1,3,6,1,4,1,171,10,120,100,1,1,1,2,1))
systemDRAMutilizationEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:systemDRAMutilizationEntry.setStatus(_A)
class _SystemDRAMutilizationUnitID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_SystemDRAMutilizationUnitID_Type.__name__=_D
_SystemDRAMutilizationUnitID_Object=MibTableColumn
systemDRAMutilizationUnitID=_SystemDRAMutilizationUnitID_Object((1,3,6,1,4,1,171,10,120,100,1,1,1,2,1,1),_SystemDRAMutilizationUnitID_Type())
systemDRAMutilizationUnitID.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:systemDRAMutilizationUnitID.setStatus(_A)
_SystemDRAMutilizationTotalDRAM_Type=Integer32
_SystemDRAMutilizationTotalDRAM_Object=MibTableColumn
systemDRAMutilizationTotalDRAM=_SystemDRAMutilizationTotalDRAM_Object((1,3,6,1,4,1,171,10,120,100,1,1,1,2,1,2),_SystemDRAMutilizationTotalDRAM_Type())
systemDRAMutilizationTotalDRAM.setMaxAccess(_B)
if mibBuilder.loadTexts:systemDRAMutilizationTotalDRAM.setStatus(_A)
if mibBuilder.loadTexts:systemDRAMutilizationTotalDRAM.setUnits(_C)
_SystemDRAMutilizationUsedDRAM_Type=Integer32
_SystemDRAMutilizationUsedDRAM_Object=MibTableColumn
systemDRAMutilizationUsedDRAM=_SystemDRAMutilizationUsedDRAM_Object((1,3,6,1,4,1,171,10,120,100,1,1,1,2,1,3),_SystemDRAMutilizationUsedDRAM_Type())
systemDRAMutilizationUsedDRAM.setMaxAccess(_B)
if mibBuilder.loadTexts:systemDRAMutilizationUsedDRAM.setStatus(_A)
if mibBuilder.loadTexts:systemDRAMutilizationUsedDRAM.setUnits(_C)
_SystemDRAMutilization_Type=Integer32
_SystemDRAMutilization_Object=MibTableColumn
systemDRAMutilization=_SystemDRAMutilization_Object((1,3,6,1,4,1,171,10,120,100,1,1,1,2,1,4),_SystemDRAMutilization_Type())
systemDRAMutilization.setMaxAccess(_B)
if mibBuilder.loadTexts:systemDRAMutilization.setStatus(_A)
_SystemFLASHutilizationTable_Object=MibTable
systemFLASHutilizationTable=_SystemFLASHutilizationTable_Object((1,3,6,1,4,1,171,10,120,100,1,1,1,3))
if mibBuilder.loadTexts:systemFLASHutilizationTable.setStatus(_A)
_SystemFLASHutilizationEntry_Object=MibTableRow
systemFLASHutilizationEntry=_SystemFLASHutilizationEntry_Object((1,3,6,1,4,1,171,10,120,100,1,1,1,3,1))
systemFLASHutilizationEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:systemFLASHutilizationEntry.setStatus(_A)
class _SystemFLASHutilizationUnitID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_SystemFLASHutilizationUnitID_Type.__name__=_D
_SystemFLASHutilizationUnitID_Object=MibTableColumn
systemFLASHutilizationUnitID=_SystemFLASHutilizationUnitID_Object((1,3,6,1,4,1,171,10,120,100,1,1,1,3,1,1),_SystemFLASHutilizationUnitID_Type())
systemFLASHutilizationUnitID.setMaxAccess(_B)
if mibBuilder.loadTexts:systemFLASHutilizationUnitID.setStatus(_A)
_SystemFLASHutilizationTotalFLASH_Type=Integer32
_SystemFLASHutilizationTotalFLASH_Object=MibTableColumn
systemFLASHutilizationTotalFLASH=_SystemFLASHutilizationTotalFLASH_Object((1,3,6,1,4,1,171,10,120,100,1,1,1,3,1,2),_SystemFLASHutilizationTotalFLASH_Type())
systemFLASHutilizationTotalFLASH.setMaxAccess(_B)
if mibBuilder.loadTexts:systemFLASHutilizationTotalFLASH.setStatus(_A)
if mibBuilder.loadTexts:systemFLASHutilizationTotalFLASH.setUnits(_C)
_SystemFLASHutilizationUsedFLASH_Type=Integer32
_SystemFLASHutilizationUsedFLASH_Object=MibTableColumn
systemFLASHutilizationUsedFLASH=_SystemFLASHutilizationUsedFLASH_Object((1,3,6,1,4,1,171,10,120,100,1,1,1,3,1,3),_SystemFLASHutilizationUsedFLASH_Type())
systemFLASHutilizationUsedFLASH.setMaxAccess(_B)
if mibBuilder.loadTexts:systemFLASHutilizationUsedFLASH.setStatus(_A)
if mibBuilder.loadTexts:systemFLASHutilizationUsedFLASH.setUnits(_C)
_SystemFLASHutilization_Type=Integer32
_SystemFLASHutilization_Object=MibTableColumn
systemFLASHutilization=_SystemFLASHutilization_Object((1,3,6,1,4,1,171,10,120,100,1,1,1,3,1,4),_SystemFLASHutilization_Type())
systemFLASHutilization.setMaxAccess(_B)
if mibBuilder.loadTexts:systemFLASHutilization.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'dgs6600SystemInfoMIB':dgs6600SystemInfoMIB,'systemBasicInfo':systemBasicInfo,'systemCPUutilization':systemCPUutilization,'systemCPUutilizationIn5sec':systemCPUutilizationIn5sec,'systemCPUutilizationIn1min':systemCPUutilizationIn1min,'systemCPUutilizationIn5min':systemCPUutilizationIn5min,'systemDRAMutilizationTable':systemDRAMutilizationTable,'systemDRAMutilizationEntry':systemDRAMutilizationEntry,_F:systemDRAMutilizationUnitID,'systemDRAMutilizationTotalDRAM':systemDRAMutilizationTotalDRAM,'systemDRAMutilizationUsedDRAM':systemDRAMutilizationUsedDRAM,'systemDRAMutilization':systemDRAMutilization,'systemFLASHutilizationTable':systemFLASHutilizationTable,'systemFLASHutilizationEntry':systemFLASHutilizationEntry,_G:systemFLASHutilizationUnitID,'systemFLASHutilizationTotalFLASH':systemFLASHutilizationTotalFLASH,'systemFLASHutilizationUsedFLASH':systemFLASHutilizationUsedFLASH,'systemFLASHutilization':systemFLASHutilization})