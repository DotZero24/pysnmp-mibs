_K='nmspmProcessPID'
_J='read-write'
_I='DisplayString'
_H='Unsigned32'
_G='nmspmCPUTotalIndex'
_F='Integer32'
_E='FS-NMS-PROCESS-MIB'
_D='percent'
_C='Gauge32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
nmsMgmt,=mibBuilder.importSymbols('FS-NMS-SMI','nmsMgmt')
EntPhysicalIndexOrZero,=mibBuilder.importSymbols('FS-NMS-TC','EntPhysicalIndexOrZero')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_C,_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','TextualConvention','TimeStamp')
nmsProcessMIB=ModuleIdentity((1,3,6,1,4,1,52642,9,109))
if mibBuilder.loadTexts:nmsProcessMIB.setRevisions(('2003-10-16 00:00',))
_NmsProcessMIBObjects_ObjectIdentity=ObjectIdentity
nmsProcessMIBObjects=_NmsProcessMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,9,109,1))
_NmspmCPU_ObjectIdentity=ObjectIdentity
nmspmCPU=_NmspmCPU_ObjectIdentity((1,3,6,1,4,1,52642,9,109,1,1))
_NmspmCPUTotalTable_Object=MibTable
nmspmCPUTotalTable=_NmspmCPUTotalTable_Object((1,3,6,1,4,1,52642,9,109,1,1,1))
if mibBuilder.loadTexts:nmspmCPUTotalTable.setStatus(_A)
_NmspmCPUTotalEntry_Object=MibTableRow
nmspmCPUTotalEntry=_NmspmCPUTotalEntry_Object((1,3,6,1,4,1,52642,9,109,1,1,1,1))
nmspmCPUTotalEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:nmspmCPUTotalEntry.setStatus(_A)
class _NmspmCPUTotalIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_NmspmCPUTotalIndex_Type.__name__=_H
_NmspmCPUTotalIndex_Object=MibTableColumn
nmspmCPUTotalIndex=_NmspmCPUTotalIndex_Object((1,3,6,1,4,1,52642,9,109,1,1,1,1,1),_NmspmCPUTotalIndex_Type())
nmspmCPUTotalIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:nmspmCPUTotalIndex.setStatus(_A)
_NmspmCPUTotalPhysicalIndex_Type=EntPhysicalIndexOrZero
_NmspmCPUTotalPhysicalIndex_Object=MibTableColumn
nmspmCPUTotalPhysicalIndex=_NmspmCPUTotalPhysicalIndex_Object((1,3,6,1,4,1,52642,9,109,1,1,1,1,2),_NmspmCPUTotalPhysicalIndex_Type())
nmspmCPUTotalPhysicalIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nmspmCPUTotalPhysicalIndex.setStatus(_A)
class _NmspmCPUTotal5sec_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_NmspmCPUTotal5sec_Type.__name__=_C
_NmspmCPUTotal5sec_Object=MibTableColumn
nmspmCPUTotal5sec=_NmspmCPUTotal5sec_Object((1,3,6,1,4,1,52642,9,109,1,1,1,1,3),_NmspmCPUTotal5sec_Type())
nmspmCPUTotal5sec.setMaxAccess(_B)
if mibBuilder.loadTexts:nmspmCPUTotal5sec.setStatus(_A)
if mibBuilder.loadTexts:nmspmCPUTotal5sec.setUnits(_D)
class _NmspmCPUTotal1min_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_NmspmCPUTotal1min_Type.__name__=_C
_NmspmCPUTotal1min_Object=MibTableColumn
nmspmCPUTotal1min=_NmspmCPUTotal1min_Object((1,3,6,1,4,1,52642,9,109,1,1,1,1,4),_NmspmCPUTotal1min_Type())
nmspmCPUTotal1min.setMaxAccess(_B)
if mibBuilder.loadTexts:nmspmCPUTotal1min.setStatus(_A)
if mibBuilder.loadTexts:nmspmCPUTotal1min.setUnits(_D)
class _NmspmCPUTotal5min_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_NmspmCPUTotal5min_Type.__name__=_C
_NmspmCPUTotal5min_Object=MibTableColumn
nmspmCPUTotal5min=_NmspmCPUTotal5min_Object((1,3,6,1,4,1,52642,9,109,1,1,1,1,5),_NmspmCPUTotal5min_Type())
nmspmCPUTotal5min.setMaxAccess(_B)
if mibBuilder.loadTexts:nmspmCPUTotal5min.setStatus(_A)
if mibBuilder.loadTexts:nmspmCPUTotal5min.setUnits(_D)
class _NmspmCPUMaxUtilization_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_NmspmCPUMaxUtilization_Type.__name__=_C
_NmspmCPUMaxUtilization_Object=MibScalar
nmspmCPUMaxUtilization=_NmspmCPUMaxUtilization_Object((1,3,6,1,4,1,52642,9,109,1,1,2),_NmspmCPUMaxUtilization_Type())
nmspmCPUMaxUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:nmspmCPUMaxUtilization.setStatus(_A)
if mibBuilder.loadTexts:nmspmCPUMaxUtilization.setUnits(_D)
class _NmspmCPUClearMaxUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('clear',1))
_NmspmCPUClearMaxUtilization_Type.__name__=_F
_NmspmCPUClearMaxUtilization_Object=MibScalar
nmspmCPUClearMaxUtilization=_NmspmCPUClearMaxUtilization_Object((1,3,6,1,4,1,52642,9,109,1,1,3),_NmspmCPUClearMaxUtilization_Type())
nmspmCPUClearMaxUtilization.setMaxAccess(_J)
if mibBuilder.loadTexts:nmspmCPUClearMaxUtilization.setStatus(_A)
if mibBuilder.loadTexts:nmspmCPUClearMaxUtilization.setUnits(_D)
_NmspmProcess_ObjectIdentity=ObjectIdentity
nmspmProcess=_NmspmProcess_ObjectIdentity((1,3,6,1,4,1,52642,9,109,1,2))
_NmspmProcessTable_Object=MibTable
nmspmProcessTable=_NmspmProcessTable_Object((1,3,6,1,4,1,52642,9,109,1,2,1))
if mibBuilder.loadTexts:nmspmProcessTable.setStatus(_A)
_NmspmProcessEntry_Object=MibTableRow
nmspmProcessEntry=_NmspmProcessEntry_Object((1,3,6,1,4,1,52642,9,109,1,2,1,1))
nmspmProcessEntry.setIndexNames((0,_E,_G),(0,_E,_K))
if mibBuilder.loadTexts:nmspmProcessEntry.setStatus(_A)
_NmspmProcessPID_Type=Unsigned32
_NmspmProcessPID_Object=MibTableColumn
nmspmProcessPID=_NmspmProcessPID_Object((1,3,6,1,4,1,52642,9,109,1,2,1,1,1),_NmspmProcessPID_Type())
nmspmProcessPID.setMaxAccess(_B)
if mibBuilder.loadTexts:nmspmProcessPID.setStatus(_A)
class _NmspmProcessName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_NmspmProcessName_Type.__name__=_I
_NmspmProcessName_Object=MibTableColumn
nmspmProcessName=_NmspmProcessName_Object((1,3,6,1,4,1,52642,9,109,1,2,1,1,2),_NmspmProcessName_Type())
nmspmProcessName.setMaxAccess(_B)
if mibBuilder.loadTexts:nmspmProcessName.setStatus(_A)
class _NmspmProcessPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,55,60,128,180,255)));namedValues=NamedValues(*(('critical',0),('veryhigh',55),('high',60),('normal',128),('low',180),('verylow',255)))
_NmspmProcessPriority_Type.__name__=_F
_NmspmProcessPriority_Object=MibTableColumn
nmspmProcessPriority=_NmspmProcessPriority_Object((1,3,6,1,4,1,52642,9,109,1,2,1,1,3),_NmspmProcessPriority_Type())
nmspmProcessPriority.setMaxAccess(_J)
if mibBuilder.loadTexts:nmspmProcessPriority.setStatus(_A)
_NmspmProcessTimeCreated_Type=TimeStamp
_NmspmProcessTimeCreated_Object=MibTableColumn
nmspmProcessTimeCreated=_NmspmProcessTimeCreated_Object((1,3,6,1,4,1,52642,9,109,1,2,1,1,4),_NmspmProcessTimeCreated_Type())
nmspmProcessTimeCreated.setMaxAccess(_B)
if mibBuilder.loadTexts:nmspmProcessTimeCreated.setStatus(_A)
_NmsProcessMIBNotifPrefix_ObjectIdentity=ObjectIdentity
nmsProcessMIBNotifPrefix=_NmsProcessMIBNotifPrefix_ObjectIdentity((1,3,6,1,4,1,52642,9,109,2))
_NmsProcessMIBNotifs_ObjectIdentity=ObjectIdentity
nmsProcessMIBNotifs=_NmsProcessMIBNotifs_ObjectIdentity((1,3,6,1,4,1,52642,9,109,2,0))
_NmsProcessMIBConformance_ObjectIdentity=ObjectIdentity
nmsProcessMIBConformance=_NmsProcessMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,9,109,3))
_NmspmCompliances_ObjectIdentity=ObjectIdentity
nmspmCompliances=_NmspmCompliances_ObjectIdentity((1,3,6,1,4,1,52642,9,109,3,1))
_NmspmGroups_ObjectIdentity=ObjectIdentity
nmspmGroups=_NmspmGroups_ObjectIdentity((1,3,6,1,4,1,52642,9,109,3,2))
mibBuilder.exportSymbols(_E,**{'nmsProcessMIB':nmsProcessMIB,'nmsProcessMIBObjects':nmsProcessMIBObjects,'nmspmCPU':nmspmCPU,'nmspmCPUTotalTable':nmspmCPUTotalTable,'nmspmCPUTotalEntry':nmspmCPUTotalEntry,_G:nmspmCPUTotalIndex,'nmspmCPUTotalPhysicalIndex':nmspmCPUTotalPhysicalIndex,'nmspmCPUTotal5sec':nmspmCPUTotal5sec,'nmspmCPUTotal1min':nmspmCPUTotal1min,'nmspmCPUTotal5min':nmspmCPUTotal5min,'nmspmCPUMaxUtilization':nmspmCPUMaxUtilization,'nmspmCPUClearMaxUtilization':nmspmCPUClearMaxUtilization,'nmspmProcess':nmspmProcess,'nmspmProcessTable':nmspmProcessTable,'nmspmProcessEntry':nmspmProcessEntry,_K:nmspmProcessPID,'nmspmProcessName':nmspmProcessName,'nmspmProcessPriority':nmspmProcessPriority,'nmspmProcessTimeCreated':nmspmProcessTimeCreated,'nmsProcessMIBNotifPrefix':nmsProcessMIBNotifPrefix,'nmsProcessMIBNotifs':nmsProcessMIBNotifs,'nmsProcessMIBConformance':nmsProcessMIBConformance,'nmspmCompliances':nmspmCompliances,'nmspmGroups':nmspmGroups})