_Y='etsysDvmrpExtTibMgrGroup'
_X='etsysDvmrpExtIfGroup'
_W='etsysDvmrpExtTibMgrSGStateStored'
_V='etsysDvmrpExtTibMgrSGStateWarnThold'
_U='etsysDvmrpExtTibMgrSGStateLimit'
_T='etsysDvmrpExtTibMgrMetric'
_S='etsysDvmrpExtTibMgrKeepalivePeriod'
_R='etsysDvmrpExtIfReportInterval'
_Q='etsysDvmrpExtIfHelloHoldtime'
_P='etsysDvmrpExtIfHelloInterval'
_O='etsysDvmrpExtIfP2PNoHellos'
_N='etsysDvmrpExtIfStubInterface'
_M='etsysDvmrpExtIfIfOperStatus'
_L='etsysDvmrpExtIfAdminStatus'
_K='etsysDvmrpExtIfEntry'
_J='read-only'
_I='etsysDvmrpExtTibMgrIndex'
_H='TruthValue'
_G='Integer32'
_F='read-write'
_E='seconds'
_D='read-create'
_C='Unsigned32'
_B='ENTERASYS-DVMRP-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dvmrpInterfaceEntry,=mibBuilder.importSymbols('DVMRP-MIB','dvmrpInterfaceEntry')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_H)
etsysDvmrpExtMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,69))
if mibBuilder.loadTexts:etsysDvmrpExtMIB.setRevisions(('2009-02-27 19:29',))
_EtsysDvmrpExtObjects_ObjectIdentity=ObjectIdentity
etsysDvmrpExtObjects=_EtsysDvmrpExtObjects_ObjectIdentity((1,3,6,1,4,1,5624,1,2,69,1))
_EtsysDvmrpExtGlobals_ObjectIdentity=ObjectIdentity
etsysDvmrpExtGlobals=_EtsysDvmrpExtGlobals_ObjectIdentity((1,3,6,1,4,1,5624,1,2,69,1,1))
_EtsysDvmrpExtTables_ObjectIdentity=ObjectIdentity
etsysDvmrpExtTables=_EtsysDvmrpExtTables_ObjectIdentity((1,3,6,1,4,1,5624,1,2,69,1,2))
_EtsysDvmrpExtIfTable_Object=MibTable
etsysDvmrpExtIfTable=_EtsysDvmrpExtIfTable_Object((1,3,6,1,4,1,5624,1,2,69,1,2,1))
if mibBuilder.loadTexts:etsysDvmrpExtIfTable.setStatus(_A)
_EtsysDvmrpExtIfEntry_Object=MibTableRow
etsysDvmrpExtIfEntry=_EtsysDvmrpExtIfEntry_Object((1,3,6,1,4,1,5624,1,2,69,1,2,1,1))
if mibBuilder.loadTexts:etsysDvmrpExtIfEntry.setStatus(_A)
class _EtsysDvmrpExtIfAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('adminStatusUp',1),('adminStatusDown',2)))
_EtsysDvmrpExtIfAdminStatus_Type.__name__=_G
_EtsysDvmrpExtIfAdminStatus_Object=MibTableColumn
etsysDvmrpExtIfAdminStatus=_EtsysDvmrpExtIfAdminStatus_Object((1,3,6,1,4,1,5624,1,2,69,1,2,1,1,1),_EtsysDvmrpExtIfAdminStatus_Type())
etsysDvmrpExtIfAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysDvmrpExtIfAdminStatus.setStatus(_A)
class _EtsysDvmrpExtIfIfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,8,10,11)));namedValues=NamedValues(*(('operStatusUp',1),('operStatusDown',2),('operStatusGoingUp',3),('operStatusGoingDown',4),('operStatusActFailed',5),('operStatusFailed',8),('operStatusFailedPerm',10),('operStatusFailing',11)))
_EtsysDvmrpExtIfIfOperStatus_Type.__name__=_G
_EtsysDvmrpExtIfIfOperStatus_Object=MibTableColumn
etsysDvmrpExtIfIfOperStatus=_EtsysDvmrpExtIfIfOperStatus_Object((1,3,6,1,4,1,5624,1,2,69,1,2,1,1,2),_EtsysDvmrpExtIfIfOperStatus_Type())
etsysDvmrpExtIfIfOperStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:etsysDvmrpExtIfIfOperStatus.setStatus(_A)
class _EtsysDvmrpExtIfStubInterface_Type(TruthValue):defaultValue=2
_EtsysDvmrpExtIfStubInterface_Type.__name__=_H
_EtsysDvmrpExtIfStubInterface_Object=MibTableColumn
etsysDvmrpExtIfStubInterface=_EtsysDvmrpExtIfStubInterface_Object((1,3,6,1,4,1,5624,1,2,69,1,2,1,1,3),_EtsysDvmrpExtIfStubInterface_Type())
etsysDvmrpExtIfStubInterface.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysDvmrpExtIfStubInterface.setStatus(_A)
class _EtsysDvmrpExtIfP2PNoHellos_Type(TruthValue):defaultValue=2
_EtsysDvmrpExtIfP2PNoHellos_Type.__name__=_H
_EtsysDvmrpExtIfP2PNoHellos_Object=MibTableColumn
etsysDvmrpExtIfP2PNoHellos=_EtsysDvmrpExtIfP2PNoHellos_Object((1,3,6,1,4,1,5624,1,2,69,1,2,1,1,4),_EtsysDvmrpExtIfP2PNoHellos_Type())
etsysDvmrpExtIfP2PNoHellos.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysDvmrpExtIfP2PNoHellos.setStatus(_A)
class _EtsysDvmrpExtIfHelloInterval_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,18000))
_EtsysDvmrpExtIfHelloInterval_Type.__name__=_C
_EtsysDvmrpExtIfHelloInterval_Object=MibTableColumn
etsysDvmrpExtIfHelloInterval=_EtsysDvmrpExtIfHelloInterval_Object((1,3,6,1,4,1,5624,1,2,69,1,2,1,1,5),_EtsysDvmrpExtIfHelloInterval_Type())
etsysDvmrpExtIfHelloInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysDvmrpExtIfHelloInterval.setStatus(_A)
if mibBuilder.loadTexts:etsysDvmrpExtIfHelloInterval.setUnits(_E)
class _EtsysDvmrpExtIfHelloHoldtime_Type(Unsigned32):defaultValue=35;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_EtsysDvmrpExtIfHelloHoldtime_Type.__name__=_C
_EtsysDvmrpExtIfHelloHoldtime_Object=MibTableColumn
etsysDvmrpExtIfHelloHoldtime=_EtsysDvmrpExtIfHelloHoldtime_Object((1,3,6,1,4,1,5624,1,2,69,1,2,1,1,6),_EtsysDvmrpExtIfHelloHoldtime_Type())
etsysDvmrpExtIfHelloHoldtime.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysDvmrpExtIfHelloHoldtime.setStatus(_A)
if mibBuilder.loadTexts:etsysDvmrpExtIfHelloHoldtime.setUnits(_E)
class _EtsysDvmrpExtIfReportInterval_Type(Unsigned32):defaultValue=60;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,18000))
_EtsysDvmrpExtIfReportInterval_Type.__name__=_C
_EtsysDvmrpExtIfReportInterval_Object=MibTableColumn
etsysDvmrpExtIfReportInterval=_EtsysDvmrpExtIfReportInterval_Object((1,3,6,1,4,1,5624,1,2,69,1,2,1,1,7),_EtsysDvmrpExtIfReportInterval_Type())
etsysDvmrpExtIfReportInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysDvmrpExtIfReportInterval.setStatus(_A)
if mibBuilder.loadTexts:etsysDvmrpExtIfReportInterval.setUnits(_E)
_EtsysDvmrpExtTibMgrTable_Object=MibTable
etsysDvmrpExtTibMgrTable=_EtsysDvmrpExtTibMgrTable_Object((1,3,6,1,4,1,5624,1,2,69,1,2,2))
if mibBuilder.loadTexts:etsysDvmrpExtTibMgrTable.setStatus(_A)
_EtsysDvmrpExtTibMgrEntry_Object=MibTableRow
etsysDvmrpExtTibMgrEntry=_EtsysDvmrpExtTibMgrEntry_Object((1,3,6,1,4,1,5624,1,2,69,1,2,2,1))
etsysDvmrpExtTibMgrEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:etsysDvmrpExtTibMgrEntry.setStatus(_A)
_EtsysDvmrpExtTibMgrIndex_Type=Unsigned32
_EtsysDvmrpExtTibMgrIndex_Object=MibTableColumn
etsysDvmrpExtTibMgrIndex=_EtsysDvmrpExtTibMgrIndex_Object((1,3,6,1,4,1,5624,1,2,69,1,2,2,1,1),_EtsysDvmrpExtTibMgrIndex_Type())
etsysDvmrpExtTibMgrIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:etsysDvmrpExtTibMgrIndex.setStatus(_A)
class _EtsysDvmrpExtTibMgrKeepalivePeriod_Type(Unsigned32):defaultValue=120;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,180))
_EtsysDvmrpExtTibMgrKeepalivePeriod_Type.__name__=_C
_EtsysDvmrpExtTibMgrKeepalivePeriod_Object=MibTableColumn
etsysDvmrpExtTibMgrKeepalivePeriod=_EtsysDvmrpExtTibMgrKeepalivePeriod_Object((1,3,6,1,4,1,5624,1,2,69,1,2,2,1,2),_EtsysDvmrpExtTibMgrKeepalivePeriod_Type())
etsysDvmrpExtTibMgrKeepalivePeriod.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysDvmrpExtTibMgrKeepalivePeriod.setStatus(_A)
if mibBuilder.loadTexts:etsysDvmrpExtTibMgrKeepalivePeriod.setUnits(_E)
class _EtsysDvmrpExtTibMgrMetric_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
_EtsysDvmrpExtTibMgrMetric_Type.__name__=_C
_EtsysDvmrpExtTibMgrMetric_Object=MibTableColumn
etsysDvmrpExtTibMgrMetric=_EtsysDvmrpExtTibMgrMetric_Object((1,3,6,1,4,1,5624,1,2,69,1,2,2,1,3),_EtsysDvmrpExtTibMgrMetric_Type())
etsysDvmrpExtTibMgrMetric.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysDvmrpExtTibMgrMetric.setStatus(_A)
class _EtsysDvmrpExtTibMgrSGStateLimit_Type(Unsigned32):defaultValue=0
_EtsysDvmrpExtTibMgrSGStateLimit_Type.__name__=_C
_EtsysDvmrpExtTibMgrSGStateLimit_Object=MibTableColumn
etsysDvmrpExtTibMgrSGStateLimit=_EtsysDvmrpExtTibMgrSGStateLimit_Object((1,3,6,1,4,1,5624,1,2,69,1,2,2,1,4),_EtsysDvmrpExtTibMgrSGStateLimit_Type())
etsysDvmrpExtTibMgrSGStateLimit.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysDvmrpExtTibMgrSGStateLimit.setStatus(_A)
class _EtsysDvmrpExtTibMgrSGStateWarnThold_Type(Unsigned32):defaultValue=0
_EtsysDvmrpExtTibMgrSGStateWarnThold_Type.__name__=_C
_EtsysDvmrpExtTibMgrSGStateWarnThold_Object=MibTableColumn
etsysDvmrpExtTibMgrSGStateWarnThold=_EtsysDvmrpExtTibMgrSGStateWarnThold_Object((1,3,6,1,4,1,5624,1,2,69,1,2,2,1,5),_EtsysDvmrpExtTibMgrSGStateWarnThold_Type())
etsysDvmrpExtTibMgrSGStateWarnThold.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysDvmrpExtTibMgrSGStateWarnThold.setStatus(_A)
_EtsysDvmrpExtTibMgrSGStateStored_Type=Gauge32
_EtsysDvmrpExtTibMgrSGStateStored_Object=MibTableColumn
etsysDvmrpExtTibMgrSGStateStored=_EtsysDvmrpExtTibMgrSGStateStored_Object((1,3,6,1,4,1,5624,1,2,69,1,2,2,1,6),_EtsysDvmrpExtTibMgrSGStateStored_Type())
etsysDvmrpExtTibMgrSGStateStored.setMaxAccess(_J)
if mibBuilder.loadTexts:etsysDvmrpExtTibMgrSGStateStored.setStatus(_A)
_EtsysDvmrpExtConformance_ObjectIdentity=ObjectIdentity
etsysDvmrpExtConformance=_EtsysDvmrpExtConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,69,2))
_EtsysDvmrpExtGroups_ObjectIdentity=ObjectIdentity
etsysDvmrpExtGroups=_EtsysDvmrpExtGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,69,2,1))
_EtsysDvmrpExtCompliances_ObjectIdentity=ObjectIdentity
etsysDvmrpExtCompliances=_EtsysDvmrpExtCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,69,2,2))
dvmrpInterfaceEntry.registerAugmentions((_B,_K))
etsysDvmrpExtIfEntry.setIndexNames(*dvmrpInterfaceEntry.getIndexNames())
etsysDvmrpExtIfGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,69,2,1,1))
etsysDvmrpExtIfGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:etsysDvmrpExtIfGroup.setStatus(_A)
etsysDvmrpExtTibMgrGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,69,2,1,2))
etsysDvmrpExtTibMgrGroup.setObjects(*((_B,_I),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:etsysDvmrpExtTibMgrGroup.setStatus(_A)
etsysDvmrpExtCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,69,2,2,1))
etsysDvmrpExtCompliance.setObjects(*((_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:etsysDvmrpExtCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'etsysDvmrpExtMIB':etsysDvmrpExtMIB,'etsysDvmrpExtObjects':etsysDvmrpExtObjects,'etsysDvmrpExtGlobals':etsysDvmrpExtGlobals,'etsysDvmrpExtTables':etsysDvmrpExtTables,'etsysDvmrpExtIfTable':etsysDvmrpExtIfTable,_K:etsysDvmrpExtIfEntry,_L:etsysDvmrpExtIfAdminStatus,_M:etsysDvmrpExtIfIfOperStatus,_N:etsysDvmrpExtIfStubInterface,_O:etsysDvmrpExtIfP2PNoHellos,_P:etsysDvmrpExtIfHelloInterval,_Q:etsysDvmrpExtIfHelloHoldtime,_R:etsysDvmrpExtIfReportInterval,'etsysDvmrpExtTibMgrTable':etsysDvmrpExtTibMgrTable,'etsysDvmrpExtTibMgrEntry':etsysDvmrpExtTibMgrEntry,_I:etsysDvmrpExtTibMgrIndex,_S:etsysDvmrpExtTibMgrKeepalivePeriod,_T:etsysDvmrpExtTibMgrMetric,_U:etsysDvmrpExtTibMgrSGStateLimit,_V:etsysDvmrpExtTibMgrSGStateWarnThold,_W:etsysDvmrpExtTibMgrSGStateStored,'etsysDvmrpExtConformance':etsysDvmrpExtConformance,'etsysDvmrpExtGroups':etsysDvmrpExtGroups,_X:etsysDvmrpExtIfGroup,_Y:etsysDvmrpExtTibMgrGroup,'etsysDvmrpExtCompliances':etsysDvmrpExtCompliances,'etsysDvmrpExtCompliance':etsysDvmrpExtCompliance})