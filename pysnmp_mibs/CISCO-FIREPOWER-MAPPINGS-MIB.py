_I='cfprMappingsDnToOidDn'
_H='cfprMappingsMoInverseContainmentParentInstanceId'
_G='cfprMappingsMoInverseContainmentChildInstanceId'
_F='cfprMappingsMoContainmentChildInstanceId'
_E='cfprMappingsMoContainmentParentInstanceId'
_D='read-only'
_C='not-accessible'
_B='CISCO-FIREPOWER-MAPPINGS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CfprManagedObjectDn,CfprManagedObjectId,ciscoFirepowerMIB=mibBuilder.importSymbols('CISCO-FIREPOWER-MIB','CfprManagedObjectDn','CfprManagedObjectId','ciscoFirepowerMIB')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cfprMappingsObjects=ModuleIdentity((1,3,6,1,4,1,9,9,826,3))
_CfprMappingsMoContainmentTable_Object=MibTable
cfprMappingsMoContainmentTable=_CfprMappingsMoContainmentTable_Object((1,3,6,1,4,1,9,9,826,3,1))
if mibBuilder.loadTexts:cfprMappingsMoContainmentTable.setStatus(_A)
_CfprMappingsMoContainmentEntry_Object=MibTableRow
cfprMappingsMoContainmentEntry=_CfprMappingsMoContainmentEntry_Object((1,3,6,1,4,1,9,9,826,3,1,1))
cfprMappingsMoContainmentEntry.setIndexNames((0,_B,_E),(0,_B,_F))
if mibBuilder.loadTexts:cfprMappingsMoContainmentEntry.setStatus(_A)
_CfprMappingsMoContainmentParentInstanceId_Type=CfprManagedObjectId
_CfprMappingsMoContainmentParentInstanceId_Object=MibTableColumn
cfprMappingsMoContainmentParentInstanceId=_CfprMappingsMoContainmentParentInstanceId_Object((1,3,6,1,4,1,9,9,826,3,1,1,1),_CfprMappingsMoContainmentParentInstanceId_Type())
cfprMappingsMoContainmentParentInstanceId.setMaxAccess(_C)
if mibBuilder.loadTexts:cfprMappingsMoContainmentParentInstanceId.setStatus(_A)
_CfprMappingsMoContainmentChildInstanceId_Type=CfprManagedObjectId
_CfprMappingsMoContainmentChildInstanceId_Object=MibTableColumn
cfprMappingsMoContainmentChildInstanceId=_CfprMappingsMoContainmentChildInstanceId_Object((1,3,6,1,4,1,9,9,826,3,1,1,2),_CfprMappingsMoContainmentChildInstanceId_Type())
cfprMappingsMoContainmentChildInstanceId.setMaxAccess(_C)
if mibBuilder.loadTexts:cfprMappingsMoContainmentChildInstanceId.setStatus(_A)
_CfprMappingsMoContainmentParentDn_Type=CfprManagedObjectDn
_CfprMappingsMoContainmentParentDn_Object=MibTableColumn
cfprMappingsMoContainmentParentDn=_CfprMappingsMoContainmentParentDn_Object((1,3,6,1,4,1,9,9,826,3,1,1,3),_CfprMappingsMoContainmentParentDn_Type())
cfprMappingsMoContainmentParentDn.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprMappingsMoContainmentParentDn.setStatus(_A)
_CfprMappingsMoContainmentChildDn_Type=CfprManagedObjectDn
_CfprMappingsMoContainmentChildDn_Object=MibTableColumn
cfprMappingsMoContainmentChildDn=_CfprMappingsMoContainmentChildDn_Object((1,3,6,1,4,1,9,9,826,3,1,1,4),_CfprMappingsMoContainmentChildDn_Type())
cfprMappingsMoContainmentChildDn.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprMappingsMoContainmentChildDn.setStatus(_A)
_CfprMappingsMoInverseContainmentTable_Object=MibTable
cfprMappingsMoInverseContainmentTable=_CfprMappingsMoInverseContainmentTable_Object((1,3,6,1,4,1,9,9,826,3,2))
if mibBuilder.loadTexts:cfprMappingsMoInverseContainmentTable.setStatus(_A)
_CfprMappingsMoInverseContainmentEntry_Object=MibTableRow
cfprMappingsMoInverseContainmentEntry=_CfprMappingsMoInverseContainmentEntry_Object((1,3,6,1,4,1,9,9,826,3,2,1))
cfprMappingsMoInverseContainmentEntry.setIndexNames((0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:cfprMappingsMoInverseContainmentEntry.setStatus(_A)
_CfprMappingsMoInverseContainmentChildInstanceId_Type=CfprManagedObjectId
_CfprMappingsMoInverseContainmentChildInstanceId_Object=MibTableColumn
cfprMappingsMoInverseContainmentChildInstanceId=_CfprMappingsMoInverseContainmentChildInstanceId_Object((1,3,6,1,4,1,9,9,826,3,2,1,1),_CfprMappingsMoInverseContainmentChildInstanceId_Type())
cfprMappingsMoInverseContainmentChildInstanceId.setMaxAccess(_C)
if mibBuilder.loadTexts:cfprMappingsMoInverseContainmentChildInstanceId.setStatus(_A)
_CfprMappingsMoInverseContainmentParentInstanceId_Type=CfprManagedObjectId
_CfprMappingsMoInverseContainmentParentInstanceId_Object=MibTableColumn
cfprMappingsMoInverseContainmentParentInstanceId=_CfprMappingsMoInverseContainmentParentInstanceId_Object((1,3,6,1,4,1,9,9,826,3,2,1,2),_CfprMappingsMoInverseContainmentParentInstanceId_Type())
cfprMappingsMoInverseContainmentParentInstanceId.setMaxAccess(_C)
if mibBuilder.loadTexts:cfprMappingsMoInverseContainmentParentInstanceId.setStatus(_A)
_CfprMappingsMoInverseContainmentParentDn_Type=CfprManagedObjectDn
_CfprMappingsMoInverseContainmentParentDn_Object=MibTableColumn
cfprMappingsMoInverseContainmentParentDn=_CfprMappingsMoInverseContainmentParentDn_Object((1,3,6,1,4,1,9,9,826,3,2,1,3),_CfprMappingsMoInverseContainmentParentDn_Type())
cfprMappingsMoInverseContainmentParentDn.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprMappingsMoInverseContainmentParentDn.setStatus(_A)
_CfprMappingsMoInverseContainmentChildDn_Type=CfprManagedObjectDn
_CfprMappingsMoInverseContainmentChildDn_Object=MibTableColumn
cfprMappingsMoInverseContainmentChildDn=_CfprMappingsMoInverseContainmentChildDn_Object((1,3,6,1,4,1,9,9,826,3,2,1,4),_CfprMappingsMoInverseContainmentChildDn_Type())
cfprMappingsMoInverseContainmentChildDn.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprMappingsMoInverseContainmentChildDn.setStatus(_A)
_CfprMappingsDnToOidTable_Object=MibTable
cfprMappingsDnToOidTable=_CfprMappingsDnToOidTable_Object((1,3,6,1,4,1,9,9,826,3,3))
if mibBuilder.loadTexts:cfprMappingsDnToOidTable.setStatus(_A)
_CfprMappingsDnToOidEntry_Object=MibTableRow
cfprMappingsDnToOidEntry=_CfprMappingsDnToOidEntry_Object((1,3,6,1,4,1,9,9,826,3,3,1))
cfprMappingsDnToOidEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:cfprMappingsDnToOidEntry.setStatus(_A)
_CfprMappingsDnToOidDn_Type=CfprManagedObjectDn
_CfprMappingsDnToOidDn_Object=MibTableColumn
cfprMappingsDnToOidDn=_CfprMappingsDnToOidDn_Object((1,3,6,1,4,1,9,9,826,3,3,1,1),_CfprMappingsDnToOidDn_Type())
cfprMappingsDnToOidDn.setMaxAccess(_C)
if mibBuilder.loadTexts:cfprMappingsDnToOidDn.setStatus(_A)
_CfprMappingsDnToOidOid_Type=RowPointer
_CfprMappingsDnToOidOid_Object=MibTableColumn
cfprMappingsDnToOidOid=_CfprMappingsDnToOidOid_Object((1,3,6,1,4,1,9,9,826,3,3,1,2),_CfprMappingsDnToOidOid_Type())
cfprMappingsDnToOidOid.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprMappingsDnToOidOid.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'cfprMappingsObjects':cfprMappingsObjects,'cfprMappingsMoContainmentTable':cfprMappingsMoContainmentTable,'cfprMappingsMoContainmentEntry':cfprMappingsMoContainmentEntry,_E:cfprMappingsMoContainmentParentInstanceId,_F:cfprMappingsMoContainmentChildInstanceId,'cfprMappingsMoContainmentParentDn':cfprMappingsMoContainmentParentDn,'cfprMappingsMoContainmentChildDn':cfprMappingsMoContainmentChildDn,'cfprMappingsMoInverseContainmentTable':cfprMappingsMoInverseContainmentTable,'cfprMappingsMoInverseContainmentEntry':cfprMappingsMoInverseContainmentEntry,_G:cfprMappingsMoInverseContainmentChildInstanceId,_H:cfprMappingsMoInverseContainmentParentInstanceId,'cfprMappingsMoInverseContainmentParentDn':cfprMappingsMoInverseContainmentParentDn,'cfprMappingsMoInverseContainmentChildDn':cfprMappingsMoInverseContainmentChildDn,'cfprMappingsDnToOidTable':cfprMappingsDnToOidTable,'cfprMappingsDnToOidEntry':cfprMappingsDnToOidEntry,_I:cfprMappingsDnToOidDn,'cfprMappingsDnToOidOid':cfprMappingsDnToOidOid})