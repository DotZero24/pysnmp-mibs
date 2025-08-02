_E='serviceId'
_D='serviceDescription'
_C='read-only'
_B='SONICWALL-SMA-APPLIANCE-SERVICE-HEALTH-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InternationalDisplayString,=mibBuilder.importSymbols('HOST-RESOURCES-MIB','InternationalDisplayString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
sonicwallSMAAppliance,=mibBuilder.importSymbols('SONICWALL-SMA-MIB','sonicwallSMAAppliance')
sonicwallServiceHealth=ModuleIdentity((1,3,6,1,4,1,8741,8,1,3))
_ServiceTable_Object=MibTable
serviceTable=_ServiceTable_Object((1,3,6,1,4,1,8741,8,1,3,1))
if mibBuilder.loadTexts:serviceTable.setStatus(_A)
_ServiceEntry_Object=MibTableRow
serviceEntry=_ServiceEntry_Object((1,3,6,1,4,1,8741,8,1,3,1,1))
serviceEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:serviceEntry.setStatus(_A)
_ServiceId_Type=Integer32
_ServiceId_Object=MibTableColumn
serviceId=_ServiceId_Object((1,3,6,1,4,1,8741,8,1,3,1,1,1),_ServiceId_Type())
serviceId.setMaxAccess(_C)
if mibBuilder.loadTexts:serviceId.setStatus(_A)
_ServiceDescription_Type=InternationalDisplayString
_ServiceDescription_Object=MibTableColumn
serviceDescription=_ServiceDescription_Object((1,3,6,1,4,1,8741,8,1,3,1,1,2),_ServiceDescription_Type())
serviceDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:serviceDescription.setStatus(_A)
_ServiceState_Type=Integer32
_ServiceState_Object=MibTableColumn
serviceState=_ServiceState_Object((1,3,6,1,4,1,8741,8,1,3,1,1,3),_ServiceState_Type())
serviceState.setMaxAccess(_C)
if mibBuilder.loadTexts:serviceState.setStatus(_A)
_ServiceTableRowStatus_Type=RowStatus
_ServiceTableRowStatus_Object=MibTableColumn
serviceTableRowStatus=_ServiceTableRowStatus_Object((1,3,6,1,4,1,8741,8,1,3,1,1,4),_ServiceTableRowStatus_Type())
serviceTableRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:serviceTableRowStatus.setStatus(_A)
asapServiceUp=NotificationType((1,3,6,1,4,1,8741,8,1,3,2))
asapServiceUp.setObjects((_B,_D))
if mibBuilder.loadTexts:asapServiceUp.setStatus(_A)
asapServiceDown=NotificationType((1,3,6,1,4,1,8741,8,1,3,3))
asapServiceDown.setObjects((_B,_D))
if mibBuilder.loadTexts:asapServiceDown.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'sonicwallServiceHealth':sonicwallServiceHealth,'serviceTable':serviceTable,'serviceEntry':serviceEntry,_E:serviceId,_D:serviceDescription,'serviceState':serviceState,'serviceTableRowStatus':serviceTableRowStatus,'asapServiceUp':asapServiceUp,'asapServiceDown':asapServiceDown})