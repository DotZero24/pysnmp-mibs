_I='cucsMappingsDnToOidDn'
_H='cucsMappingsMoInverseContainmentParentInstanceId'
_G='cucsMappingsMoInverseContainmentChildInstanceId'
_F='cucsMappingsMoContainmentChildInstanceId'
_E='cucsMappingsMoContainmentParentInstanceId'
_D='read-only'
_C='not-accessible'
_B='CISCO-UNIFIED-COMPUTING-MAPPINGS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
CucsManagedObjectDn,CucsManagedObjectId,ciscoUnifiedComputingMIB=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-MIB','CucsManagedObjectDn','CucsManagedObjectId','ciscoUnifiedComputingMIB')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cucsMappingsObjects=ModuleIdentity((1,3,6,1,4,1,9,9,719,3))
_CucsMappingsMoContainmentTable_Object=MibTable
cucsMappingsMoContainmentTable=_CucsMappingsMoContainmentTable_Object((1,3,6,1,4,1,9,9,719,3,1))
if mibBuilder.loadTexts:cucsMappingsMoContainmentTable.setStatus(_A)
_CucsMappingsMoContainmentEntry_Object=MibTableRow
cucsMappingsMoContainmentEntry=_CucsMappingsMoContainmentEntry_Object((1,3,6,1,4,1,9,9,719,3,1,1))
cucsMappingsMoContainmentEntry.setIndexNames((0,_B,_E),(0,_B,_F))
if mibBuilder.loadTexts:cucsMappingsMoContainmentEntry.setStatus(_A)
_CucsMappingsMoContainmentParentInstanceId_Type=CucsManagedObjectId
_CucsMappingsMoContainmentParentInstanceId_Object=MibTableColumn
cucsMappingsMoContainmentParentInstanceId=_CucsMappingsMoContainmentParentInstanceId_Object((1,3,6,1,4,1,9,9,719,3,1,1,1),_CucsMappingsMoContainmentParentInstanceId_Type())
cucsMappingsMoContainmentParentInstanceId.setMaxAccess(_C)
if mibBuilder.loadTexts:cucsMappingsMoContainmentParentInstanceId.setStatus(_A)
_CucsMappingsMoContainmentChildInstanceId_Type=CucsManagedObjectId
_CucsMappingsMoContainmentChildInstanceId_Object=MibTableColumn
cucsMappingsMoContainmentChildInstanceId=_CucsMappingsMoContainmentChildInstanceId_Object((1,3,6,1,4,1,9,9,719,3,1,1,2),_CucsMappingsMoContainmentChildInstanceId_Type())
cucsMappingsMoContainmentChildInstanceId.setMaxAccess(_C)
if mibBuilder.loadTexts:cucsMappingsMoContainmentChildInstanceId.setStatus(_A)
_CucsMappingsMoContainmentParentDn_Type=CucsManagedObjectDn
_CucsMappingsMoContainmentParentDn_Object=MibTableColumn
cucsMappingsMoContainmentParentDn=_CucsMappingsMoContainmentParentDn_Object((1,3,6,1,4,1,9,9,719,3,1,1,3),_CucsMappingsMoContainmentParentDn_Type())
cucsMappingsMoContainmentParentDn.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsMappingsMoContainmentParentDn.setStatus(_A)
_CucsMappingsMoContainmentChildDn_Type=CucsManagedObjectDn
_CucsMappingsMoContainmentChildDn_Object=MibTableColumn
cucsMappingsMoContainmentChildDn=_CucsMappingsMoContainmentChildDn_Object((1,3,6,1,4,1,9,9,719,3,1,1,4),_CucsMappingsMoContainmentChildDn_Type())
cucsMappingsMoContainmentChildDn.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsMappingsMoContainmentChildDn.setStatus(_A)
_CucsMappingsMoInverseContainmentTable_Object=MibTable
cucsMappingsMoInverseContainmentTable=_CucsMappingsMoInverseContainmentTable_Object((1,3,6,1,4,1,9,9,719,3,2))
if mibBuilder.loadTexts:cucsMappingsMoInverseContainmentTable.setStatus(_A)
_CucsMappingsMoInverseContainmentEntry_Object=MibTableRow
cucsMappingsMoInverseContainmentEntry=_CucsMappingsMoInverseContainmentEntry_Object((1,3,6,1,4,1,9,9,719,3,2,1))
cucsMappingsMoInverseContainmentEntry.setIndexNames((0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:cucsMappingsMoInverseContainmentEntry.setStatus(_A)
_CucsMappingsMoInverseContainmentChildInstanceId_Type=CucsManagedObjectId
_CucsMappingsMoInverseContainmentChildInstanceId_Object=MibTableColumn
cucsMappingsMoInverseContainmentChildInstanceId=_CucsMappingsMoInverseContainmentChildInstanceId_Object((1,3,6,1,4,1,9,9,719,3,2,1,1),_CucsMappingsMoInverseContainmentChildInstanceId_Type())
cucsMappingsMoInverseContainmentChildInstanceId.setMaxAccess(_C)
if mibBuilder.loadTexts:cucsMappingsMoInverseContainmentChildInstanceId.setStatus(_A)
_CucsMappingsMoInverseContainmentParentInstanceId_Type=CucsManagedObjectId
_CucsMappingsMoInverseContainmentParentInstanceId_Object=MibTableColumn
cucsMappingsMoInverseContainmentParentInstanceId=_CucsMappingsMoInverseContainmentParentInstanceId_Object((1,3,6,1,4,1,9,9,719,3,2,1,2),_CucsMappingsMoInverseContainmentParentInstanceId_Type())
cucsMappingsMoInverseContainmentParentInstanceId.setMaxAccess(_C)
if mibBuilder.loadTexts:cucsMappingsMoInverseContainmentParentInstanceId.setStatus(_A)
_CucsMappingsMoInverseContainmentParentDn_Type=CucsManagedObjectDn
_CucsMappingsMoInverseContainmentParentDn_Object=MibTableColumn
cucsMappingsMoInverseContainmentParentDn=_CucsMappingsMoInverseContainmentParentDn_Object((1,3,6,1,4,1,9,9,719,3,2,1,3),_CucsMappingsMoInverseContainmentParentDn_Type())
cucsMappingsMoInverseContainmentParentDn.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsMappingsMoInverseContainmentParentDn.setStatus(_A)
_CucsMappingsMoInverseContainmentChildDn_Type=CucsManagedObjectDn
_CucsMappingsMoInverseContainmentChildDn_Object=MibTableColumn
cucsMappingsMoInverseContainmentChildDn=_CucsMappingsMoInverseContainmentChildDn_Object((1,3,6,1,4,1,9,9,719,3,2,1,4),_CucsMappingsMoInverseContainmentChildDn_Type())
cucsMappingsMoInverseContainmentChildDn.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsMappingsMoInverseContainmentChildDn.setStatus(_A)
_CucsMappingsDnToOidTable_Object=MibTable
cucsMappingsDnToOidTable=_CucsMappingsDnToOidTable_Object((1,3,6,1,4,1,9,9,719,3,3))
if mibBuilder.loadTexts:cucsMappingsDnToOidTable.setStatus(_A)
_CucsMappingsDnToOidEntry_Object=MibTableRow
cucsMappingsDnToOidEntry=_CucsMappingsDnToOidEntry_Object((1,3,6,1,4,1,9,9,719,3,3,1))
cucsMappingsDnToOidEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:cucsMappingsDnToOidEntry.setStatus(_A)
_CucsMappingsDnToOidDn_Type=CucsManagedObjectDn
_CucsMappingsDnToOidDn_Object=MibTableColumn
cucsMappingsDnToOidDn=_CucsMappingsDnToOidDn_Object((1,3,6,1,4,1,9,9,719,3,3,1,1),_CucsMappingsDnToOidDn_Type())
cucsMappingsDnToOidDn.setMaxAccess(_C)
if mibBuilder.loadTexts:cucsMappingsDnToOidDn.setStatus(_A)
_CucsMappingsDnToOidOid_Type=RowPointer
_CucsMappingsDnToOidOid_Object=MibTableColumn
cucsMappingsDnToOidOid=_CucsMappingsDnToOidOid_Object((1,3,6,1,4,1,9,9,719,3,3,1,2),_CucsMappingsDnToOidOid_Type())
cucsMappingsDnToOidOid.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsMappingsDnToOidOid.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'cucsMappingsObjects':cucsMappingsObjects,'cucsMappingsMoContainmentTable':cucsMappingsMoContainmentTable,'cucsMappingsMoContainmentEntry':cucsMappingsMoContainmentEntry,_E:cucsMappingsMoContainmentParentInstanceId,_F:cucsMappingsMoContainmentChildInstanceId,'cucsMappingsMoContainmentParentDn':cucsMappingsMoContainmentParentDn,'cucsMappingsMoContainmentChildDn':cucsMappingsMoContainmentChildDn,'cucsMappingsMoInverseContainmentTable':cucsMappingsMoInverseContainmentTable,'cucsMappingsMoInverseContainmentEntry':cucsMappingsMoInverseContainmentEntry,_G:cucsMappingsMoInverseContainmentChildInstanceId,_H:cucsMappingsMoInverseContainmentParentInstanceId,'cucsMappingsMoInverseContainmentParentDn':cucsMappingsMoInverseContainmentParentDn,'cucsMappingsMoInverseContainmentChildDn':cucsMappingsMoInverseContainmentChildDn,'cucsMappingsDnToOidTable':cucsMappingsDnToOidTable,'cucsMappingsDnToOidEntry':cucsMappingsDnToOidEntry,_I:cucsMappingsDnToOidDn,'cucsMappingsDnToOidOid':cucsMappingsDnToOidOid})