_I='ligoPingTime'
_H='read-only'
_G='not-accessible'
_F='ligoPingAddr'
_E='ligoPingAddrType'
_D='LIGO-GENERIC-MIB'
_C='sysLocation'
_B='SNMPv2-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ligoMgmt,=mibBuilder.importSymbols('LIGOWAVE-MIB','ligoMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysLocation,=mibBuilder.importSymbols(_B,_C)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ligoGenericMIB=ModuleIdentity((1,3,6,1,4,1,32750,3,1))
if mibBuilder.loadTexts:ligoGenericMIB.setRevisions(('2016-01-15 00:00','2009-02-13 00:00'))
_LigoGenericMIBObjects_ObjectIdentity=ObjectIdentity
ligoGenericMIBObjects=_LigoGenericMIBObjects_ObjectIdentity((1,3,6,1,4,1,32750,3,1,1))
_LigoGenericNotifs_ObjectIdentity=ObjectIdentity
ligoGenericNotifs=_LigoGenericNotifs_ObjectIdentity((1,3,6,1,4,1,32750,3,1,1,0))
_LigoGenericInfo_ObjectIdentity=ObjectIdentity
ligoGenericInfo=_LigoGenericInfo_ObjectIdentity((1,3,6,1,4,1,32750,3,1,1,1))
_LigoPingHostsTable_Object=MibTable
ligoPingHostsTable=_LigoPingHostsTable_Object((1,3,6,1,4,1,32750,3,1,1,1,2))
if mibBuilder.loadTexts:ligoPingHostsTable.setStatus(_A)
_LigoPingHostsEntry_Object=MibTableRow
ligoPingHostsEntry=_LigoPingHostsEntry_Object((1,3,6,1,4,1,32750,3,1,1,1,2,1))
ligoPingHostsEntry.setIndexNames((0,_D,_E),(0,_D,_F))
if mibBuilder.loadTexts:ligoPingHostsEntry.setStatus(_A)
_LigoPingAddrType_Type=InetAddressType
_LigoPingAddrType_Object=MibTableColumn
ligoPingAddrType=_LigoPingAddrType_Object((1,3,6,1,4,1,32750,3,1,1,1,2,1,1),_LigoPingAddrType_Type())
ligoPingAddrType.setMaxAccess(_G)
if mibBuilder.loadTexts:ligoPingAddrType.setStatus(_A)
_LigoPingAddr_Type=InetAddress
_LigoPingAddr_Object=MibTableColumn
ligoPingAddr=_LigoPingAddr_Object((1,3,6,1,4,1,32750,3,1,1,1,2,1,2),_LigoPingAddr_Type())
ligoPingAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:ligoPingAddr.setStatus(_A)
_LigoPingTime_Type=Integer32
_LigoPingTime_Object=MibTableColumn
ligoPingTime=_LigoPingTime_Object((1,3,6,1,4,1,32750,3,1,1,1,2,1,3),_LigoPingTime_Type())
ligoPingTime.setMaxAccess(_H)
if mibBuilder.loadTexts:ligoPingTime.setStatus(_A)
if mibBuilder.loadTexts:ligoPingTime.setUnits('ms')
_LigoPingHost_Type=DisplayString
_LigoPingHost_Object=MibTableColumn
ligoPingHost=_LigoPingHost_Object((1,3,6,1,4,1,32750,3,1,1,1,2,1,4),_LigoPingHost_Type())
ligoPingHost.setMaxAccess(_H)
if mibBuilder.loadTexts:ligoPingHost.setStatus(_A)
ligoPowerLoss=NotificationType((1,3,6,1,4,1,32750,3,1,1,0,1))
ligoPowerLoss.setObjects((_B,_C))
if mibBuilder.loadTexts:ligoPowerLoss.setStatus(_A)
ligoAdministrativeReboot=NotificationType((1,3,6,1,4,1,32750,3,1,1,0,2))
ligoAdministrativeReboot.setObjects((_B,_C))
if mibBuilder.loadTexts:ligoAdministrativeReboot.setStatus(_A)
ligoHeartbeat=NotificationType((1,3,6,1,4,1,32750,3,1,1,0,3))
ligoHeartbeat.setObjects((_B,_C))
if mibBuilder.loadTexts:ligoHeartbeat.setStatus(_A)
ligoHighPing=NotificationType((1,3,6,1,4,1,32750,3,1,1,0,4))
ligoHighPing.setObjects(*((_B,_C),(_D,_I)))
if mibBuilder.loadTexts:ligoHighPing.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'ligoGenericMIB':ligoGenericMIB,'ligoGenericMIBObjects':ligoGenericMIBObjects,'ligoGenericNotifs':ligoGenericNotifs,'ligoPowerLoss':ligoPowerLoss,'ligoAdministrativeReboot':ligoAdministrativeReboot,'ligoHeartbeat':ligoHeartbeat,'ligoHighPing':ligoHighPing,'ligoGenericInfo':ligoGenericInfo,'ligoPingHostsTable':ligoPingHostsTable,'ligoPingHostsEntry':ligoPingHostsEntry,_E:ligoPingAddrType,_F:ligoPingAddr,_I:ligoPingTime,'ligoPingHost':ligoPingHost})