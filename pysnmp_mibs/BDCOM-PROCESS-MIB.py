_J='bdpmProcessPID'
_I='DisplayString'
_H='Unsigned32'
_G='Integer32'
_F='percent'
_E='bdpmCPUTotalIndex'
_D='BDCOM-PROCESS-MIB'
_C='Gauge32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
bdMgmt,=mibBuilder.importSymbols('BDCOM-SMI','bdMgmt')
EntPhysicalIndexOrZero,=mibBuilder.importSymbols('BDCOM-TC','EntPhysicalIndexOrZero')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_C,_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','TextualConvention','TimeStamp')
bdcomProcessMIB=ModuleIdentity((1,3,6,1,4,1,3320,9,109))
if mibBuilder.loadTexts:bdcomProcessMIB.setRevisions(('2003-10-16 00:00',))
_BdcomProcessMIBObjects_ObjectIdentity=ObjectIdentity
bdcomProcessMIBObjects=_BdcomProcessMIBObjects_ObjectIdentity((1,3,6,1,4,1,3320,9,109,1))
_BdpmCPU_ObjectIdentity=ObjectIdentity
bdpmCPU=_BdpmCPU_ObjectIdentity((1,3,6,1,4,1,3320,9,109,1,1))
_BdpmCPUTotalTable_Object=MibTable
bdpmCPUTotalTable=_BdpmCPUTotalTable_Object((1,3,6,1,4,1,3320,9,109,1,1,1))
if mibBuilder.loadTexts:bdpmCPUTotalTable.setStatus(_A)
_BdpmCPUTotalEntry_Object=MibTableRow
bdpmCPUTotalEntry=_BdpmCPUTotalEntry_Object((1,3,6,1,4,1,3320,9,109,1,1,1,1))
bdpmCPUTotalEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:bdpmCPUTotalEntry.setStatus(_A)
class _BdpmCPUTotalIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_BdpmCPUTotalIndex_Type.__name__=_H
_BdpmCPUTotalIndex_Object=MibTableColumn
bdpmCPUTotalIndex=_BdpmCPUTotalIndex_Object((1,3,6,1,4,1,3320,9,109,1,1,1,1,1),_BdpmCPUTotalIndex_Type())
bdpmCPUTotalIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:bdpmCPUTotalIndex.setStatus(_A)
_BdpmCPUTotalPhysicalIndex_Type=EntPhysicalIndexOrZero
_BdpmCPUTotalPhysicalIndex_Object=MibTableColumn
bdpmCPUTotalPhysicalIndex=_BdpmCPUTotalPhysicalIndex_Object((1,3,6,1,4,1,3320,9,109,1,1,1,1,2),_BdpmCPUTotalPhysicalIndex_Type())
bdpmCPUTotalPhysicalIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:bdpmCPUTotalPhysicalIndex.setStatus(_A)
class _BdpmCPUTotal5sec_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_BdpmCPUTotal5sec_Type.__name__=_C
_BdpmCPUTotal5sec_Object=MibTableColumn
bdpmCPUTotal5sec=_BdpmCPUTotal5sec_Object((1,3,6,1,4,1,3320,9,109,1,1,1,1,3),_BdpmCPUTotal5sec_Type())
bdpmCPUTotal5sec.setMaxAccess(_B)
if mibBuilder.loadTexts:bdpmCPUTotal5sec.setStatus(_A)
if mibBuilder.loadTexts:bdpmCPUTotal5sec.setUnits(_F)
class _BdpmCPUTotal1min_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_BdpmCPUTotal1min_Type.__name__=_C
_BdpmCPUTotal1min_Object=MibTableColumn
bdpmCPUTotal1min=_BdpmCPUTotal1min_Object((1,3,6,1,4,1,3320,9,109,1,1,1,1,4),_BdpmCPUTotal1min_Type())
bdpmCPUTotal1min.setMaxAccess(_B)
if mibBuilder.loadTexts:bdpmCPUTotal1min.setStatus(_A)
if mibBuilder.loadTexts:bdpmCPUTotal1min.setUnits(_F)
class _BdpmCPUTotal5min_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_BdpmCPUTotal5min_Type.__name__=_C
_BdpmCPUTotal5min_Object=MibTableColumn
bdpmCPUTotal5min=_BdpmCPUTotal5min_Object((1,3,6,1,4,1,3320,9,109,1,1,1,1,5),_BdpmCPUTotal5min_Type())
bdpmCPUTotal5min.setMaxAccess(_B)
if mibBuilder.loadTexts:bdpmCPUTotal5min.setStatus(_A)
if mibBuilder.loadTexts:bdpmCPUTotal5min.setUnits(_F)
_BdpmProcess_ObjectIdentity=ObjectIdentity
bdpmProcess=_BdpmProcess_ObjectIdentity((1,3,6,1,4,1,3320,9,109,1,2))
_BdpmProcessTable_Object=MibTable
bdpmProcessTable=_BdpmProcessTable_Object((1,3,6,1,4,1,3320,9,109,1,2,1))
if mibBuilder.loadTexts:bdpmProcessTable.setStatus(_A)
_BdpmProcessEntry_Object=MibTableRow
bdpmProcessEntry=_BdpmProcessEntry_Object((1,3,6,1,4,1,3320,9,109,1,2,1,1))
bdpmProcessEntry.setIndexNames((0,_D,_E),(0,_D,_J))
if mibBuilder.loadTexts:bdpmProcessEntry.setStatus(_A)
_BdpmProcessPID_Type=Unsigned32
_BdpmProcessPID_Object=MibTableColumn
bdpmProcessPID=_BdpmProcessPID_Object((1,3,6,1,4,1,3320,9,109,1,2,1,1,1),_BdpmProcessPID_Type())
bdpmProcessPID.setMaxAccess(_B)
if mibBuilder.loadTexts:bdpmProcessPID.setStatus(_A)
class _BdpmProcessName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_BdpmProcessName_Type.__name__=_I
_BdpmProcessName_Object=MibTableColumn
bdpmProcessName=_BdpmProcessName_Object((1,3,6,1,4,1,3320,9,109,1,2,1,1,2),_BdpmProcessName_Type())
bdpmProcessName.setMaxAccess(_B)
if mibBuilder.loadTexts:bdpmProcessName.setStatus(_A)
class _BdpmProcessPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,55,60,128,180,255)));namedValues=NamedValues(*(('critical',0),('veryhigh',55),('high',60),('normal',128),('low',180),('verylow',255)))
_BdpmProcessPriority_Type.__name__=_G
_BdpmProcessPriority_Object=MibTableColumn
bdpmProcessPriority=_BdpmProcessPriority_Object((1,3,6,1,4,1,3320,9,109,1,2,1,1,3),_BdpmProcessPriority_Type())
bdpmProcessPriority.setMaxAccess('read-write')
if mibBuilder.loadTexts:bdpmProcessPriority.setStatus(_A)
_BdpmProcessTimeCreated_Type=TimeStamp
_BdpmProcessTimeCreated_Object=MibTableColumn
bdpmProcessTimeCreated=_BdpmProcessTimeCreated_Object((1,3,6,1,4,1,3320,9,109,1,2,1,1,4),_BdpmProcessTimeCreated_Type())
bdpmProcessTimeCreated.setMaxAccess(_B)
if mibBuilder.loadTexts:bdpmProcessTimeCreated.setStatus(_A)
_BdcomProcessMIBNotifPrefix_ObjectIdentity=ObjectIdentity
bdcomProcessMIBNotifPrefix=_BdcomProcessMIBNotifPrefix_ObjectIdentity((1,3,6,1,4,1,3320,9,109,2))
_BdcomProcessMIBNotifs_ObjectIdentity=ObjectIdentity
bdcomProcessMIBNotifs=_BdcomProcessMIBNotifs_ObjectIdentity((1,3,6,1,4,1,3320,9,109,2,0))
mibBuilder.exportSymbols(_D,**{'bdcomProcessMIB':bdcomProcessMIB,'bdcomProcessMIBObjects':bdcomProcessMIBObjects,'bdpmCPU':bdpmCPU,'bdpmCPUTotalTable':bdpmCPUTotalTable,'bdpmCPUTotalEntry':bdpmCPUTotalEntry,_E:bdpmCPUTotalIndex,'bdpmCPUTotalPhysicalIndex':bdpmCPUTotalPhysicalIndex,'bdpmCPUTotal5sec':bdpmCPUTotal5sec,'bdpmCPUTotal1min':bdpmCPUTotal1min,'bdpmCPUTotal5min':bdpmCPUTotal5min,'bdpmProcess':bdpmProcess,'bdpmProcessTable':bdpmProcessTable,'bdpmProcessEntry':bdpmProcessEntry,_J:bdpmProcessPID,'bdpmProcessName':bdpmProcessName,'bdpmProcessPriority':bdpmProcessPriority,'bdpmProcessTimeCreated':bdpmProcessTimeCreated,'bdcomProcessMIBNotifPrefix':bdcomProcessMIBNotifPrefix,'bdcomProcessMIBNotifs':bdcomProcessMIBNotifs})