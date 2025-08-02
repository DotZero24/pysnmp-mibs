_F='cucsOrgSourceMaskInstanceId'
_E='not-accessible'
_D='cucsOrgOrgInstanceId'
_C='CISCO-UNIFIED-COMPUTING-ORG-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
CucsManagedObjectDn,CucsManagedObjectId,ciscoUnifiedComputingMIBObjects=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-MIB','CucsManagedObjectDn','CucsManagedObjectId','ciscoUnifiedComputingMIBObjects')
CucsOrgLevel,CucsOrgSrcMask=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-TC-MIB','CucsOrgLevel','CucsOrgSrcMask')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cucsOrgObjects=ModuleIdentity((1,3,6,1,4,1,9,9,719,1,34))
_CucsOrgOrgTable_Object=MibTable
cucsOrgOrgTable=_CucsOrgOrgTable_Object((1,3,6,1,4,1,9,9,719,1,34,1))
if mibBuilder.loadTexts:cucsOrgOrgTable.setStatus(_A)
_CucsOrgOrgEntry_Object=MibTableRow
cucsOrgOrgEntry=_CucsOrgOrgEntry_Object((1,3,6,1,4,1,9,9,719,1,34,1,1))
cucsOrgOrgEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:cucsOrgOrgEntry.setStatus(_A)
_CucsOrgOrgInstanceId_Type=CucsManagedObjectId
_CucsOrgOrgInstanceId_Object=MibTableColumn
cucsOrgOrgInstanceId=_CucsOrgOrgInstanceId_Object((1,3,6,1,4,1,9,9,719,1,34,1,1,1),_CucsOrgOrgInstanceId_Type())
cucsOrgOrgInstanceId.setMaxAccess(_E)
if mibBuilder.loadTexts:cucsOrgOrgInstanceId.setStatus(_A)
_CucsOrgOrgDn_Type=CucsManagedObjectDn
_CucsOrgOrgDn_Object=MibTableColumn
cucsOrgOrgDn=_CucsOrgOrgDn_Object((1,3,6,1,4,1,9,9,719,1,34,1,1,2),_CucsOrgOrgDn_Type())
cucsOrgOrgDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsOrgOrgDn.setStatus(_A)
_CucsOrgOrgRn_Type=SnmpAdminString
_CucsOrgOrgRn_Object=MibTableColumn
cucsOrgOrgRn=_CucsOrgOrgRn_Object((1,3,6,1,4,1,9,9,719,1,34,1,1,3),_CucsOrgOrgRn_Type())
cucsOrgOrgRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsOrgOrgRn.setStatus(_A)
_CucsOrgOrgDescr_Type=SnmpAdminString
_CucsOrgOrgDescr_Object=MibTableColumn
cucsOrgOrgDescr=_CucsOrgOrgDescr_Object((1,3,6,1,4,1,9,9,719,1,34,1,1,4),_CucsOrgOrgDescr_Type())
cucsOrgOrgDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsOrgOrgDescr.setStatus(_A)
_CucsOrgOrgFltAggr_Type=Unsigned64
_CucsOrgOrgFltAggr_Object=MibTableColumn
cucsOrgOrgFltAggr=_CucsOrgOrgFltAggr_Object((1,3,6,1,4,1,9,9,719,1,34,1,1,5),_CucsOrgOrgFltAggr_Type())
cucsOrgOrgFltAggr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsOrgOrgFltAggr.setStatus(_A)
_CucsOrgOrgLevel_Type=CucsOrgLevel
_CucsOrgOrgLevel_Object=MibTableColumn
cucsOrgOrgLevel=_CucsOrgOrgLevel_Object((1,3,6,1,4,1,9,9,719,1,34,1,1,6),_CucsOrgOrgLevel_Type())
cucsOrgOrgLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsOrgOrgLevel.setStatus(_A)
_CucsOrgOrgName_Type=SnmpAdminString
_CucsOrgOrgName_Object=MibTableColumn
cucsOrgOrgName=_CucsOrgOrgName_Object((1,3,6,1,4,1,9,9,719,1,34,1,1,7),_CucsOrgOrgName_Type())
cucsOrgOrgName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsOrgOrgName.setStatus(_A)
_CucsOrgOrgPermAccess_Type=TruthValue
_CucsOrgOrgPermAccess_Object=MibTableColumn
cucsOrgOrgPermAccess=_CucsOrgOrgPermAccess_Object((1,3,6,1,4,1,9,9,719,1,34,1,1,8),_CucsOrgOrgPermAccess_Type())
cucsOrgOrgPermAccess.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsOrgOrgPermAccess.setStatus(_A)
_CucsOrgSourceMaskTable_Object=MibTable
cucsOrgSourceMaskTable=_CucsOrgSourceMaskTable_Object((1,3,6,1,4,1,9,9,719,1,34,2))
if mibBuilder.loadTexts:cucsOrgSourceMaskTable.setStatus(_A)
_CucsOrgSourceMaskEntry_Object=MibTableRow
cucsOrgSourceMaskEntry=_CucsOrgSourceMaskEntry_Object((1,3,6,1,4,1,9,9,719,1,34,2,1))
cucsOrgSourceMaskEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cucsOrgSourceMaskEntry.setStatus(_A)
_CucsOrgSourceMaskInstanceId_Type=CucsManagedObjectId
_CucsOrgSourceMaskInstanceId_Object=MibTableColumn
cucsOrgSourceMaskInstanceId=_CucsOrgSourceMaskInstanceId_Object((1,3,6,1,4,1,9,9,719,1,34,2,1,1),_CucsOrgSourceMaskInstanceId_Type())
cucsOrgSourceMaskInstanceId.setMaxAccess(_E)
if mibBuilder.loadTexts:cucsOrgSourceMaskInstanceId.setStatus(_A)
_CucsOrgSourceMaskDn_Type=CucsManagedObjectDn
_CucsOrgSourceMaskDn_Object=MibTableColumn
cucsOrgSourceMaskDn=_CucsOrgSourceMaskDn_Object((1,3,6,1,4,1,9,9,719,1,34,2,1,2),_CucsOrgSourceMaskDn_Type())
cucsOrgSourceMaskDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsOrgSourceMaskDn.setStatus(_A)
_CucsOrgSourceMaskRn_Type=SnmpAdminString
_CucsOrgSourceMaskRn_Object=MibTableColumn
cucsOrgSourceMaskRn=_CucsOrgSourceMaskRn_Object((1,3,6,1,4,1,9,9,719,1,34,2,1,3),_CucsOrgSourceMaskRn_Type())
cucsOrgSourceMaskRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsOrgSourceMaskRn.setStatus(_A)
_CucsOrgSourceMaskMask_Type=CucsOrgSrcMask
_CucsOrgSourceMaskMask_Object=MibTableColumn
cucsOrgSourceMaskMask=_CucsOrgSourceMaskMask_Object((1,3,6,1,4,1,9,9,719,1,34,2,1,4),_CucsOrgSourceMaskMask_Type())
cucsOrgSourceMaskMask.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsOrgSourceMaskMask.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cucsOrgObjects':cucsOrgObjects,'cucsOrgOrgTable':cucsOrgOrgTable,'cucsOrgOrgEntry':cucsOrgOrgEntry,_D:cucsOrgOrgInstanceId,'cucsOrgOrgDn':cucsOrgOrgDn,'cucsOrgOrgRn':cucsOrgOrgRn,'cucsOrgOrgDescr':cucsOrgOrgDescr,'cucsOrgOrgFltAggr':cucsOrgOrgFltAggr,'cucsOrgOrgLevel':cucsOrgOrgLevel,'cucsOrgOrgName':cucsOrgOrgName,'cucsOrgOrgPermAccess':cucsOrgOrgPermAccess,'cucsOrgSourceMaskTable':cucsOrgSourceMaskTable,'cucsOrgSourceMaskEntry':cucsOrgSourceMaskEntry,_F:cucsOrgSourceMaskInstanceId,'cucsOrgSourceMaskDn':cucsOrgSourceMaskDn,'cucsOrgSourceMaskRn':cucsOrgSourceMaskRn,'cucsOrgSourceMaskMask':cucsOrgSourceMaskMask})