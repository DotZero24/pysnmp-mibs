_E='ruckusEventSetErrorOID'
_D='accessible-for-notify'
_C='ruckusEventClientMacAddr'
_B='RUCKUS-EVENT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ruckusEvents,=mibBuilder.importSymbols('RUCKUS-ROOT-MIB','ruckusEvents')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
ruckusEventMIB=ModuleIdentity((1,3,6,1,4,1,25053,2,1))
_RuckusEventTraps_ObjectIdentity=ObjectIdentity
ruckusEventTraps=_RuckusEventTraps_ObjectIdentity((1,3,6,1,4,1,25053,2,1,1))
_RuckusEventObjects_ObjectIdentity=ObjectIdentity
ruckusEventObjects=_RuckusEventObjects_ObjectIdentity((1,3,6,1,4,1,25053,2,1,2))
_RuckusEventClientMacAddr_Type=OctetString
_RuckusEventClientMacAddr_Object=MibScalar
ruckusEventClientMacAddr=_RuckusEventClientMacAddr_Object((1,3,6,1,4,1,25053,2,1,2,15),_RuckusEventClientMacAddr_Type())
ruckusEventClientMacAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:ruckusEventClientMacAddr.setStatus(_A)
_RuckusEventSetErrorOID_Type=ObjectIdentifier
_RuckusEventSetErrorOID_Object=MibScalar
ruckusEventSetErrorOID=_RuckusEventSetErrorOID_Object((1,3,6,1,4,1,25053,2,1,2,20),_RuckusEventSetErrorOID_Type())
ruckusEventSetErrorOID.setMaxAccess(_D)
if mibBuilder.loadTexts:ruckusEventSetErrorOID.setStatus(_A)
ruckusEventAssocTrap=NotificationType((1,3,6,1,4,1,25053,2,1,1,1))
ruckusEventAssocTrap.setObjects((_B,_C))
if mibBuilder.loadTexts:ruckusEventAssocTrap.setStatus(_A)
ruckusEventDiassocTrap=NotificationType((1,3,6,1,4,1,25053,2,1,1,2))
ruckusEventDiassocTrap.setObjects((_B,_C))
if mibBuilder.loadTexts:ruckusEventDiassocTrap.setStatus(_A)
ruckusEventSetErrorTrap=NotificationType((1,3,6,1,4,1,25053,2,1,1,3))
ruckusEventSetErrorTrap.setObjects((_B,_E))
if mibBuilder.loadTexts:ruckusEventSetErrorTrap.setStatus(_A)
ruckusEventConnectTrap=NotificationType((1,3,6,1,4,1,25053,2,1,1,25))
ruckusEventConnectTrap.setObjects((_B,_C))
if mibBuilder.loadTexts:ruckusEventConnectTrap.setStatus(_A)
ruckusEventDisconnectTrap=NotificationType((1,3,6,1,4,1,25053,2,1,1,26))
ruckusEventDisconnectTrap.setObjects((_B,_C))
if mibBuilder.loadTexts:ruckusEventDisconnectTrap.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ruckusEventMIB':ruckusEventMIB,'ruckusEventTraps':ruckusEventTraps,'ruckusEventAssocTrap':ruckusEventAssocTrap,'ruckusEventDiassocTrap':ruckusEventDiassocTrap,'ruckusEventSetErrorTrap':ruckusEventSetErrorTrap,'ruckusEventConnectTrap':ruckusEventConnectTrap,'ruckusEventDisconnectTrap':ruckusEventDisconnectTrap,'ruckusEventObjects':ruckusEventObjects,_C:ruckusEventClientMacAddr,_E:ruckusEventSetErrorOID})