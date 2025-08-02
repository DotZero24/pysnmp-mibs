_E='fsPatchCmpntIndex'
_D='fsPatchDevIndex'
_C='FS-PATCH-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
ConfigStatus,IfIndex=mibBuilder.importSymbols('FS-TC','ConfigStatus','IfIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
fsPatchMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,151))
if mibBuilder.loadTexts:fsPatchMIB.setRevisions(('2016-09-23 00:00',))
_FsPatchMIBObjects_ObjectIdentity=ObjectIdentity
fsPatchMIBObjects=_FsPatchMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,151,1))
_FsPatchTable_Object=MibTable
fsPatchTable=_FsPatchTable_Object((1,3,6,1,4,1,52642,1,1,10,2,151,1,1))
if mibBuilder.loadTexts:fsPatchTable.setStatus(_A)
_FsPatchEntry_Object=MibTableRow
fsPatchEntry=_FsPatchEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,151,1,1,1))
fsPatchEntry.setIndexNames((0,_C,_D),(0,_C,_E))
if mibBuilder.loadTexts:fsPatchEntry.setStatus(_A)
_FsPatchDevIndex_Type=Integer32
_FsPatchDevIndex_Object=MibTableColumn
fsPatchDevIndex=_FsPatchDevIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,151,1,1,1,1),_FsPatchDevIndex_Type())
fsPatchDevIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPatchDevIndex.setStatus(_A)
_FsPatchCmpntIndex_Type=Integer32
_FsPatchCmpntIndex_Object=MibTableColumn
fsPatchCmpntIndex=_FsPatchCmpntIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,151,1,1,1,2),_FsPatchCmpntIndex_Type())
fsPatchCmpntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPatchCmpntIndex.setStatus(_A)
_FsPatchDevId_Type=Integer32
_FsPatchDevId_Object=MibTableColumn
fsPatchDevId=_FsPatchDevId_Object((1,3,6,1,4,1,52642,1,1,10,2,151,1,1,1,3),_FsPatchDevId_Type())
fsPatchDevId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPatchDevId.setStatus(_A)
_FsPatchSlotId_Type=Integer32
_FsPatchSlotId_Object=MibTableColumn
fsPatchSlotId=_FsPatchSlotId_Object((1,3,6,1,4,1,52642,1,1,10,2,151,1,1,1,4),_FsPatchSlotId_Type())
fsPatchSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPatchSlotId.setStatus(_A)
_FsPatchCpuId_Type=Integer32
_FsPatchCpuId_Object=MibTableColumn
fsPatchCpuId=_FsPatchCpuId_Object((1,3,6,1,4,1,52642,1,1,10,2,151,1,1,1,5),_FsPatchCpuId_Type())
fsPatchCpuId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPatchCpuId.setStatus(_A)
_FsPatchExist_Type=DisplayString
_FsPatchExist_Object=MibTableColumn
fsPatchExist=_FsPatchExist_Object((1,3,6,1,4,1,52642,1,1,10,2,151,1,1,1,6),_FsPatchExist_Type())
fsPatchExist.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPatchExist.setStatus(_A)
_FsPatchName_Type=DisplayString
_FsPatchName_Object=MibTableColumn
fsPatchName=_FsPatchName_Object((1,3,6,1,4,1,52642,1,1,10,2,151,1,1,1,7),_FsPatchName_Type())
fsPatchName.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPatchName.setStatus(_A)
_FsPatchBranch_Type=DisplayString
_FsPatchBranch_Object=MibTableColumn
fsPatchBranch=_FsPatchBranch_Object((1,3,6,1,4,1,52642,1,1,10,2,151,1,1,1,8),_FsPatchBranch_Type())
fsPatchBranch.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPatchBranch.setStatus(_A)
_FsPatchCmpntName_Type=DisplayString
_FsPatchCmpntName_Object=MibTableColumn
fsPatchCmpntName=_FsPatchCmpntName_Object((1,3,6,1,4,1,52642,1,1,10,2,151,1,1,1,9),_FsPatchCmpntName_Type())
fsPatchCmpntName.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPatchCmpntName.setStatus(_A)
_FsPatchSize_Type=Counter64
_FsPatchSize_Object=MibTableColumn
fsPatchSize=_FsPatchSize_Object((1,3,6,1,4,1,52642,1,1,10,2,151,1,1,1,10),_FsPatchSize_Type())
fsPatchSize.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPatchSize.setStatus(_A)
_FsPatchStatus_Type=DisplayString
_FsPatchStatus_Object=MibTableColumn
fsPatchStatus=_FsPatchStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,151,1,1,1,11),_FsPatchStatus_Type())
fsPatchStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPatchStatus.setStatus(_A)
_FsPatchVersion_Type=DisplayString
_FsPatchVersion_Object=MibTableColumn
fsPatchVersion=_FsPatchVersion_Object((1,3,6,1,4,1,52642,1,1,10,2,151,1,1,1,12),_FsPatchVersion_Type())
fsPatchVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPatchVersion.setStatus(_A)
_FsPatchInstallTime_Type=DisplayString
_FsPatchInstallTime_Object=MibTableColumn
fsPatchInstallTime=_FsPatchInstallTime_Object((1,3,6,1,4,1,52642,1,1,10,2,151,1,1,1,13),_FsPatchInstallTime_Type())
fsPatchInstallTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPatchInstallTime.setStatus(_A)
_FsPatchDescription_Type=DisplayString
_FsPatchDescription_Object=MibTableColumn
fsPatchDescription=_FsPatchDescription_Object((1,3,6,1,4,1,52642,1,1,10,2,151,1,1,1,14),_FsPatchDescription_Type())
fsPatchDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPatchDescription.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'fsPatchMIB':fsPatchMIB,'fsPatchMIBObjects':fsPatchMIBObjects,'fsPatchTable':fsPatchTable,'fsPatchEntry':fsPatchEntry,_D:fsPatchDevIndex,_E:fsPatchCmpntIndex,'fsPatchDevId':fsPatchDevId,'fsPatchSlotId':fsPatchSlotId,'fsPatchCpuId':fsPatchCpuId,'fsPatchExist':fsPatchExist,'fsPatchName':fsPatchName,'fsPatchBranch':fsPatchBranch,'fsPatchCmpntName':fsPatchCmpntName,'fsPatchSize':fsPatchSize,'fsPatchStatus':fsPatchStatus,'fsPatchVersion':fsPatchVersion,'fsPatchInstallTime':fsPatchInstallTime,'fsPatchDescription':fsPatchDescription})