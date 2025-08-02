_S='hpmpMemoryGroup'
_R='hpmpCPUGroup'
_Q='hpmpMemPctInUse'
_P='hpmpMemTotal'
_O='hpmpMemInUse'
_N='hpmpMemDescr'
_M='hpmpCPUPctBusy'
_L='hpmpCPULoad15min'
_K='hpmpCPULoad5min'
_J='hpmpCPULoad1min'
_I='Kbytes'
_H='hpmpMemIndex'
_G='percent'
_F='not-accessible'
_E='hpmpCPUIndex'
_D='Unsigned32'
_C='read-only'
_B='HP-MEMPROC-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpProcurveCommon,=mibBuilder.importSymbols('HP-BASE-MIB','hpProcurveCommon')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,Opaque,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','Opaque','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
hpMemprocMIB=ModuleIdentity((1,3,6,1,4,1,11,2,3,7,11,17,7,1,5))
if mibBuilder.loadTexts:hpMemprocMIB.setRevisions(('2005-02-01 14:55',))
class Float(TextualConvention,Opaque):status=_A;subtypeSpec=Opaque.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(7,7));fixedLength=7
_HpMemprocMIBObjects_ObjectIdentity=ObjectIdentity
hpMemprocMIBObjects=_HpMemprocMIBObjects_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,17,7,1,5,1))
_HpmpCPU_ObjectIdentity=ObjectIdentity
hpmpCPU=_HpmpCPU_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,17,7,1,5,1,1))
_HpmpCPUTable_Object=MibTable
hpmpCPUTable=_HpmpCPUTable_Object((1,3,6,1,4,1,11,2,3,7,11,17,7,1,5,1,1,1))
if mibBuilder.loadTexts:hpmpCPUTable.setStatus(_A)
_HpmpCPUEntry_Object=MibTableRow
hpmpCPUEntry=_HpmpCPUEntry_Object((1,3,6,1,4,1,11,2,3,7,11,17,7,1,5,1,1,1,1))
hpmpCPUEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:hpmpCPUEntry.setStatus(_A)
class _HpmpCPUIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_HpmpCPUIndex_Type.__name__=_D
_HpmpCPUIndex_Object=MibTableColumn
hpmpCPUIndex=_HpmpCPUIndex_Object((1,3,6,1,4,1,11,2,3,7,11,17,7,1,5,1,1,1,1,1),_HpmpCPUIndex_Type())
hpmpCPUIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpmpCPUIndex.setStatus(_A)
_HpmpCPULoad1min_Type=Integer32
_HpmpCPULoad1min_Object=MibTableColumn
hpmpCPULoad1min=_HpmpCPULoad1min_Object((1,3,6,1,4,1,11,2,3,7,11,17,7,1,5,1,1,1,1,2),_HpmpCPULoad1min_Type())
hpmpCPULoad1min.setMaxAccess(_C)
if mibBuilder.loadTexts:hpmpCPULoad1min.setStatus(_A)
_HpmpCPULoad5min_Type=Integer32
_HpmpCPULoad5min_Object=MibTableColumn
hpmpCPULoad5min=_HpmpCPULoad5min_Object((1,3,6,1,4,1,11,2,3,7,11,17,7,1,5,1,1,1,1,3),_HpmpCPULoad5min_Type())
hpmpCPULoad5min.setMaxAccess(_C)
if mibBuilder.loadTexts:hpmpCPULoad5min.setStatus(_A)
_HpmpCPULoad15min_Type=Integer32
_HpmpCPULoad15min_Object=MibTableColumn
hpmpCPULoad15min=_HpmpCPULoad15min_Object((1,3,6,1,4,1,11,2,3,7,11,17,7,1,5,1,1,1,1,4),_HpmpCPULoad15min_Type())
hpmpCPULoad15min.setMaxAccess(_C)
if mibBuilder.loadTexts:hpmpCPULoad15min.setStatus(_A)
_HpmpCPUPctBusy_Type=Gauge32
_HpmpCPUPctBusy_Object=MibTableColumn
hpmpCPUPctBusy=_HpmpCPUPctBusy_Object((1,3,6,1,4,1,11,2,3,7,11,17,7,1,5,1,1,1,1,5),_HpmpCPUPctBusy_Type())
hpmpCPUPctBusy.setMaxAccess(_C)
if mibBuilder.loadTexts:hpmpCPUPctBusy.setStatus(_A)
if mibBuilder.loadTexts:hpmpCPUPctBusy.setUnits(_G)
_HpmpMemory_ObjectIdentity=ObjectIdentity
hpmpMemory=_HpmpMemory_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,17,7,1,5,1,2))
_HpmpMemTable_Object=MibTable
hpmpMemTable=_HpmpMemTable_Object((1,3,6,1,4,1,11,2,3,7,11,17,7,1,5,1,2,1))
if mibBuilder.loadTexts:hpmpMemTable.setStatus(_A)
_HpmpMemEntry_Object=MibTableRow
hpmpMemEntry=_HpmpMemEntry_Object((1,3,6,1,4,1,11,2,3,7,11,17,7,1,5,1,2,1,1))
hpmpMemEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:hpmpMemEntry.setStatus(_A)
class _HpmpMemIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_HpmpMemIndex_Type.__name__=_D
_HpmpMemIndex_Object=MibTableColumn
hpmpMemIndex=_HpmpMemIndex_Object((1,3,6,1,4,1,11,2,3,7,11,17,7,1,5,1,2,1,1,1),_HpmpMemIndex_Type())
hpmpMemIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpmpMemIndex.setStatus(_A)
_HpmpMemDescr_Type=DisplayString
_HpmpMemDescr_Object=MibTableColumn
hpmpMemDescr=_HpmpMemDescr_Object((1,3,6,1,4,1,11,2,3,7,11,17,7,1,5,1,2,1,1,2),_HpmpMemDescr_Type())
hpmpMemDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:hpmpMemDescr.setStatus(_A)
_HpmpMemInUse_Type=Unsigned32
_HpmpMemInUse_Object=MibTableColumn
hpmpMemInUse=_HpmpMemInUse_Object((1,3,6,1,4,1,11,2,3,7,11,17,7,1,5,1,2,1,1,3),_HpmpMemInUse_Type())
hpmpMemInUse.setMaxAccess(_C)
if mibBuilder.loadTexts:hpmpMemInUse.setStatus(_A)
if mibBuilder.loadTexts:hpmpMemInUse.setUnits(_I)
_HpmpMemTotal_Type=Unsigned32
_HpmpMemTotal_Object=MibTableColumn
hpmpMemTotal=_HpmpMemTotal_Object((1,3,6,1,4,1,11,2,3,7,11,17,7,1,5,1,2,1,1,4),_HpmpMemTotal_Type())
hpmpMemTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:hpmpMemTotal.setStatus(_A)
if mibBuilder.loadTexts:hpmpMemTotal.setUnits(_I)
_HpmpMemPctInUse_Type=Gauge32
_HpmpMemPctInUse_Object=MibTableColumn
hpmpMemPctInUse=_HpmpMemPctInUse_Object((1,3,6,1,4,1,11,2,3,7,11,17,7,1,5,1,2,1,1,5),_HpmpMemPctInUse_Type())
hpmpMemPctInUse.setMaxAccess(_C)
if mibBuilder.loadTexts:hpmpMemPctInUse.setStatus(_A)
if mibBuilder.loadTexts:hpmpMemPctInUse.setUnits(_G)
_HpMemprocNotificationsPrefix_ObjectIdentity=ObjectIdentity
hpMemprocNotificationsPrefix=_HpMemprocNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,17,7,1,5,2))
_HpMemprocNotifications_ObjectIdentity=ObjectIdentity
hpMemprocNotifications=_HpMemprocNotifications_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,17,7,1,5,2,0))
_HpMemprocMIBConformance_ObjectIdentity=ObjectIdentity
hpMemprocMIBConformance=_HpMemprocMIBConformance_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,17,7,1,5,3))
_HpmpCompliances_ObjectIdentity=ObjectIdentity
hpmpCompliances=_HpmpCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,17,7,1,5,3,1))
_HpmpGroups_ObjectIdentity=ObjectIdentity
hpmpGroups=_HpmpGroups_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,17,7,1,5,3,2))
hpmpCPUGroup=ObjectGroup((1,3,6,1,4,1,11,2,3,7,11,17,7,1,5,3,2,1))
hpmpCPUGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:hpmpCPUGroup.setStatus(_A)
hpmpMemoryGroup=ObjectGroup((1,3,6,1,4,1,11,2,3,7,11,17,7,1,5,3,2,2))
hpmpMemoryGroup.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:hpmpMemoryGroup.setStatus(_A)
hpMemprocMIBCompliance1=ModuleCompliance((1,3,6,1,4,1,11,2,3,7,11,17,7,1,5,3,1,1))
hpMemprocMIBCompliance1.setObjects(*((_B,_R),(_B,_S)))
if mibBuilder.loadTexts:hpMemprocMIBCompliance1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'Float':Float,'hpMemprocMIB':hpMemprocMIB,'hpMemprocMIBObjects':hpMemprocMIBObjects,'hpmpCPU':hpmpCPU,'hpmpCPUTable':hpmpCPUTable,'hpmpCPUEntry':hpmpCPUEntry,_E:hpmpCPUIndex,_J:hpmpCPULoad1min,_K:hpmpCPULoad5min,_L:hpmpCPULoad15min,_M:hpmpCPUPctBusy,'hpmpMemory':hpmpMemory,'hpmpMemTable':hpmpMemTable,'hpmpMemEntry':hpmpMemEntry,_H:hpmpMemIndex,_N:hpmpMemDescr,_O:hpmpMemInUse,_P:hpmpMemTotal,_Q:hpmpMemPctInUse,'hpMemprocNotificationsPrefix':hpMemprocNotificationsPrefix,'hpMemprocNotifications':hpMemprocNotifications,'hpMemprocMIBConformance':hpMemprocMIBConformance,'hpmpCompliances':hpmpCompliances,'hpMemprocMIBCompliance1':hpMemprocMIBCompliance1,'hpmpGroups':hpmpGroups,_R:hpmpCPUGroup,_S:hpmpMemoryGroup})