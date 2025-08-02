_F='cfprOrgSourceMaskInstanceId'
_E='not-accessible'
_D='cfprOrgOrgInstanceId'
_C='CISCO-FIREPOWER-ORG-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CfprManagedObjectDn,CfprManagedObjectId,ciscoFirepowerMIBObjects=mibBuilder.importSymbols('CISCO-FIREPOWER-MIB','CfprManagedObjectDn','CfprManagedObjectId','ciscoFirepowerMIBObjects')
CfprOrgLevel,CfprOrgSrcMask=mibBuilder.importSymbols('CISCO-FIREPOWER-TC-MIB','CfprOrgLevel','CfprOrgSrcMask')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cfprOrgObjects=ModuleIdentity((1,3,6,1,4,1,9,9,826,1,58))
_CfprOrgOrgTable_Object=MibTable
cfprOrgOrgTable=_CfprOrgOrgTable_Object((1,3,6,1,4,1,9,9,826,1,58,1))
if mibBuilder.loadTexts:cfprOrgOrgTable.setStatus(_A)
_CfprOrgOrgEntry_Object=MibTableRow
cfprOrgOrgEntry=_CfprOrgOrgEntry_Object((1,3,6,1,4,1,9,9,826,1,58,1,1))
cfprOrgOrgEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:cfprOrgOrgEntry.setStatus(_A)
_CfprOrgOrgInstanceId_Type=CfprManagedObjectId
_CfprOrgOrgInstanceId_Object=MibTableColumn
cfprOrgOrgInstanceId=_CfprOrgOrgInstanceId_Object((1,3,6,1,4,1,9,9,826,1,58,1,1,1),_CfprOrgOrgInstanceId_Type())
cfprOrgOrgInstanceId.setMaxAccess(_E)
if mibBuilder.loadTexts:cfprOrgOrgInstanceId.setStatus(_A)
_CfprOrgOrgDn_Type=CfprManagedObjectDn
_CfprOrgOrgDn_Object=MibTableColumn
cfprOrgOrgDn=_CfprOrgOrgDn_Object((1,3,6,1,4,1,9,9,826,1,58,1,1,2),_CfprOrgOrgDn_Type())
cfprOrgOrgDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOrgOrgDn.setStatus(_A)
_CfprOrgOrgRn_Type=SnmpAdminString
_CfprOrgOrgRn_Object=MibTableColumn
cfprOrgOrgRn=_CfprOrgOrgRn_Object((1,3,6,1,4,1,9,9,826,1,58,1,1,3),_CfprOrgOrgRn_Type())
cfprOrgOrgRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOrgOrgRn.setStatus(_A)
_CfprOrgOrgDescr_Type=SnmpAdminString
_CfprOrgOrgDescr_Object=MibTableColumn
cfprOrgOrgDescr=_CfprOrgOrgDescr_Object((1,3,6,1,4,1,9,9,826,1,58,1,1,4),_CfprOrgOrgDescr_Type())
cfprOrgOrgDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOrgOrgDescr.setStatus(_A)
_CfprOrgOrgFltAggr_Type=Unsigned64
_CfprOrgOrgFltAggr_Object=MibTableColumn
cfprOrgOrgFltAggr=_CfprOrgOrgFltAggr_Object((1,3,6,1,4,1,9,9,826,1,58,1,1,5),_CfprOrgOrgFltAggr_Type())
cfprOrgOrgFltAggr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOrgOrgFltAggr.setStatus(_A)
_CfprOrgOrgLevel_Type=CfprOrgLevel
_CfprOrgOrgLevel_Object=MibTableColumn
cfprOrgOrgLevel=_CfprOrgOrgLevel_Object((1,3,6,1,4,1,9,9,826,1,58,1,1,6),_CfprOrgOrgLevel_Type())
cfprOrgOrgLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOrgOrgLevel.setStatus(_A)
_CfprOrgOrgName_Type=SnmpAdminString
_CfprOrgOrgName_Object=MibTableColumn
cfprOrgOrgName=_CfprOrgOrgName_Object((1,3,6,1,4,1,9,9,826,1,58,1,1,7),_CfprOrgOrgName_Type())
cfprOrgOrgName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOrgOrgName.setStatus(_A)
_CfprOrgOrgPermAccess_Type=TruthValue
_CfprOrgOrgPermAccess_Object=MibTableColumn
cfprOrgOrgPermAccess=_CfprOrgOrgPermAccess_Object((1,3,6,1,4,1,9,9,826,1,58,1,1,8),_CfprOrgOrgPermAccess_Type())
cfprOrgOrgPermAccess.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOrgOrgPermAccess.setStatus(_A)
_CfprOrgSourceMaskTable_Object=MibTable
cfprOrgSourceMaskTable=_CfprOrgSourceMaskTable_Object((1,3,6,1,4,1,9,9,826,1,58,2))
if mibBuilder.loadTexts:cfprOrgSourceMaskTable.setStatus(_A)
_CfprOrgSourceMaskEntry_Object=MibTableRow
cfprOrgSourceMaskEntry=_CfprOrgSourceMaskEntry_Object((1,3,6,1,4,1,9,9,826,1,58,2,1))
cfprOrgSourceMaskEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cfprOrgSourceMaskEntry.setStatus(_A)
_CfprOrgSourceMaskInstanceId_Type=CfprManagedObjectId
_CfprOrgSourceMaskInstanceId_Object=MibTableColumn
cfprOrgSourceMaskInstanceId=_CfprOrgSourceMaskInstanceId_Object((1,3,6,1,4,1,9,9,826,1,58,2,1,1),_CfprOrgSourceMaskInstanceId_Type())
cfprOrgSourceMaskInstanceId.setMaxAccess(_E)
if mibBuilder.loadTexts:cfprOrgSourceMaskInstanceId.setStatus(_A)
_CfprOrgSourceMaskDn_Type=CfprManagedObjectDn
_CfprOrgSourceMaskDn_Object=MibTableColumn
cfprOrgSourceMaskDn=_CfprOrgSourceMaskDn_Object((1,3,6,1,4,1,9,9,826,1,58,2,1,2),_CfprOrgSourceMaskDn_Type())
cfprOrgSourceMaskDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOrgSourceMaskDn.setStatus(_A)
_CfprOrgSourceMaskRn_Type=SnmpAdminString
_CfprOrgSourceMaskRn_Object=MibTableColumn
cfprOrgSourceMaskRn=_CfprOrgSourceMaskRn_Object((1,3,6,1,4,1,9,9,826,1,58,2,1,3),_CfprOrgSourceMaskRn_Type())
cfprOrgSourceMaskRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOrgSourceMaskRn.setStatus(_A)
_CfprOrgSourceMaskMask_Type=CfprOrgSrcMask
_CfprOrgSourceMaskMask_Object=MibTableColumn
cfprOrgSourceMaskMask=_CfprOrgSourceMaskMask_Object((1,3,6,1,4,1,9,9,826,1,58,2,1,4),_CfprOrgSourceMaskMask_Type())
cfprOrgSourceMaskMask.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOrgSourceMaskMask.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cfprOrgObjects':cfprOrgObjects,'cfprOrgOrgTable':cfprOrgOrgTable,'cfprOrgOrgEntry':cfprOrgOrgEntry,_D:cfprOrgOrgInstanceId,'cfprOrgOrgDn':cfprOrgOrgDn,'cfprOrgOrgRn':cfprOrgOrgRn,'cfprOrgOrgDescr':cfprOrgOrgDescr,'cfprOrgOrgFltAggr':cfprOrgOrgFltAggr,'cfprOrgOrgLevel':cfprOrgOrgLevel,'cfprOrgOrgName':cfprOrgOrgName,'cfprOrgOrgPermAccess':cfprOrgOrgPermAccess,'cfprOrgSourceMaskTable':cfprOrgSourceMaskTable,'cfprOrgSourceMaskEntry':cfprOrgSourceMaskEntry,_F:cfprOrgSourceMaskInstanceId,'cfprOrgSourceMaskDn':cfprOrgSourceMaskDn,'cfprOrgSourceMaskRn':cfprOrgSourceMaskRn,'cfprOrgSourceMaskMask':cfprOrgSourceMaskMask})