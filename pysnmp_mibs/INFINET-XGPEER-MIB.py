_G='xgPeerGroup'
_F='xgPeerSysName'
_E='xgPeerSerialNumber'
_D='xgPeerIpAddress'
_C='read-only'
_B='INFINET-XGPEER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
xg,=mibBuilder.importSymbols('INFINET-XG-MIB','xg')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
xgPeer=ModuleIdentity((1,3,6,1,4,1,3942,4,1,2))
if mibBuilder.loadTexts:xgPeer.setRevisions(('2015-10-08 08:35',))
_XgPeerSerialNumber_Type=Integer32
_XgPeerSerialNumber_Object=MibScalar
xgPeerSerialNumber=_XgPeerSerialNumber_Object((1,3,6,1,4,1,3942,4,1,2,1),_XgPeerSerialNumber_Type())
xgPeerSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:xgPeerSerialNumber.setStatus(_A)
_XgPeerSysName_Type=DisplayString
_XgPeerSysName_Object=MibScalar
xgPeerSysName=_XgPeerSysName_Object((1,3,6,1,4,1,3942,4,1,2,2),_XgPeerSysName_Type())
xgPeerSysName.setMaxAccess(_C)
if mibBuilder.loadTexts:xgPeerSysName.setStatus(_A)
_XgPeerIpAddrTable_Object=MibTable
xgPeerIpAddrTable=_XgPeerIpAddrTable_Object((1,3,6,1,4,1,3942,4,1,2,3))
if mibBuilder.loadTexts:xgPeerIpAddrTable.setStatus(_A)
_XgPeerIpAddrEntry_Object=MibTableRow
xgPeerIpAddrEntry=_XgPeerIpAddrEntry_Object((1,3,6,1,4,1,3942,4,1,2,3,1))
xgPeerIpAddrEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:xgPeerIpAddrEntry.setStatus(_A)
_XgPeerIpAddress_Type=IpAddress
_XgPeerIpAddress_Object=MibTableColumn
xgPeerIpAddress=_XgPeerIpAddress_Object((1,3,6,1,4,1,3942,4,1,2,3,1,1),_XgPeerIpAddress_Type())
xgPeerIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:xgPeerIpAddress.setStatus(_A)
_XgPeerMIBConformance_ObjectIdentity=ObjectIdentity
xgPeerMIBConformance=_XgPeerMIBConformance_ObjectIdentity((1,3,6,1,4,1,3942,4,1,2,10))
_XgPeerMIBCompliances_ObjectIdentity=ObjectIdentity
xgPeerMIBCompliances=_XgPeerMIBCompliances_ObjectIdentity((1,3,6,1,4,1,3942,4,1,2,10,1))
_XgPeerMIBGroups_ObjectIdentity=ObjectIdentity
xgPeerMIBGroups=_XgPeerMIBGroups_ObjectIdentity((1,3,6,1,4,1,3942,4,1,2,10,2))
xgPeerGroup=ObjectGroup((1,3,6,1,4,1,3942,4,1,2,10,2,1))
xgPeerGroup.setObjects(*((_B,_E),(_B,_F),(_B,_D)))
if mibBuilder.loadTexts:xgPeerGroup.setStatus(_A)
xgPeerMIBCompliance=ModuleCompliance((1,3,6,1,4,1,3942,4,1,2,10,1,1))
xgPeerMIBCompliance.setObjects((_B,_G))
if mibBuilder.loadTexts:xgPeerMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'xgPeer':xgPeer,_E:xgPeerSerialNumber,_F:xgPeerSysName,'xgPeerIpAddrTable':xgPeerIpAddrTable,'xgPeerIpAddrEntry':xgPeerIpAddrEntry,_D:xgPeerIpAddress,'xgPeerMIBConformance':xgPeerMIBConformance,'xgPeerMIBCompliances':xgPeerMIBCompliances,'xgPeerMIBCompliance':xgPeerMIBCompliance,'xgPeerMIBGroups':xgPeerMIBGroups,_G:xgPeerGroup})