_D='esiServerName'
_C='WLSX-ESI-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
wlsxEnterpriseMibModules,=mibBuilder.importSymbols('ARUBA-MIB','wlsxEnterpriseMibModules')
ArubaESIServerMode,ArubaESIServerStatus=mibBuilder.importSymbols('ARUBA-TC','ArubaESIServerMode','ArubaESIServerStatus')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,snmpModules=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','snmpModules')
DisplayString,MacAddress,PhysAddress,RowStatus,StorageType,TAddress,TDomain,TextualConvention,TestAndIncr,TimeInterval,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','StorageType','TAddress','TDomain','TextualConvention','TestAndIncr','TimeInterval','TruthValue')
wlsxESIMIB=ModuleIdentity((1,3,6,1,4,1,14823,2,2,1,10))
if mibBuilder.loadTexts:wlsxESIMIB.setRevisions(('2020-08-14 17:45',))
_WlsxESIConfigGroup_ObjectIdentity=ObjectIdentity
wlsxESIConfigGroup=_WlsxESIConfigGroup_ObjectIdentity((1,3,6,1,4,1,14823,2,2,1,10,1))
_WlsxESIServerTable_Object=MibTable
wlsxESIServerTable=_WlsxESIServerTable_Object((1,3,6,1,4,1,14823,2,2,1,10,1,1))
if mibBuilder.loadTexts:wlsxESIServerTable.setStatus(_A)
_WlsxESIServerEntry_Object=MibTableRow
wlsxESIServerEntry=_WlsxESIServerEntry_Object((1,3,6,1,4,1,14823,2,2,1,10,1,1,1))
wlsxESIServerEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:wlsxESIServerEntry.setStatus(_A)
_EsiServerName_Type=DisplayString
_EsiServerName_Object=MibTableColumn
esiServerName=_EsiServerName_Object((1,3,6,1,4,1,14823,2,2,1,10,1,1,1,1),_EsiServerName_Type())
esiServerName.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:esiServerName.setStatus(_A)
_EsiServerGroup_Type=DisplayString
_EsiServerGroup_Object=MibTableColumn
esiServerGroup=_EsiServerGroup_Object((1,3,6,1,4,1,14823,2,2,1,10,1,1,1,2),_EsiServerGroup_Type())
esiServerGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:esiServerGroup.setStatus(_A)
_EsiServerMode_Type=ArubaESIServerMode
_EsiServerMode_Object=MibTableColumn
esiServerMode=_EsiServerMode_Object((1,3,6,1,4,1,14823,2,2,1,10,1,1,1,3),_EsiServerMode_Type())
esiServerMode.setMaxAccess(_B)
if mibBuilder.loadTexts:esiServerMode.setStatus(_A)
_EsiServerTrustedIP_Type=IpAddress
_EsiServerTrustedIP_Object=MibTableColumn
esiServerTrustedIP=_EsiServerTrustedIP_Object((1,3,6,1,4,1,14823,2,2,1,10,1,1,1,4),_EsiServerTrustedIP_Type())
esiServerTrustedIP.setMaxAccess(_B)
if mibBuilder.loadTexts:esiServerTrustedIP.setStatus(_A)
_EsiServerUntrustedIP_Type=IpAddress
_EsiServerUntrustedIP_Object=MibTableColumn
esiServerUntrustedIP=_EsiServerUntrustedIP_Object((1,3,6,1,4,1,14823,2,2,1,10,1,1,1,5),_EsiServerUntrustedIP_Type())
esiServerUntrustedIP.setMaxAccess(_B)
if mibBuilder.loadTexts:esiServerUntrustedIP.setStatus(_A)
_EsiServerTrustedSlot_Type=Integer32
_EsiServerTrustedSlot_Object=MibTableColumn
esiServerTrustedSlot=_EsiServerTrustedSlot_Object((1,3,6,1,4,1,14823,2,2,1,10,1,1,1,6),_EsiServerTrustedSlot_Type())
esiServerTrustedSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:esiServerTrustedSlot.setStatus(_A)
_EsiServerTrustedPort_Type=Integer32
_EsiServerTrustedPort_Object=MibTableColumn
esiServerTrustedPort=_EsiServerTrustedPort_Object((1,3,6,1,4,1,14823,2,2,1,10,1,1,1,7),_EsiServerTrustedPort_Type())
esiServerTrustedPort.setMaxAccess(_B)
if mibBuilder.loadTexts:esiServerTrustedPort.setStatus(_A)
_EsiServerUntrustedSlot_Type=Integer32
_EsiServerUntrustedSlot_Object=MibTableColumn
esiServerUntrustedSlot=_EsiServerUntrustedSlot_Object((1,3,6,1,4,1,14823,2,2,1,10,1,1,1,8),_EsiServerUntrustedSlot_Type())
esiServerUntrustedSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:esiServerUntrustedSlot.setStatus(_A)
_EsiServerUntrustedPort_Type=Integer32
_EsiServerUntrustedPort_Object=MibTableColumn
esiServerUntrustedPort=_EsiServerUntrustedPort_Object((1,3,6,1,4,1,14823,2,2,1,10,1,1,1,9),_EsiServerUntrustedPort_Type())
esiServerUntrustedPort.setMaxAccess(_B)
if mibBuilder.loadTexts:esiServerUntrustedPort.setStatus(_A)
_EsiServerStatus_Type=ArubaESIServerStatus
_EsiServerStatus_Object=MibTableColumn
esiServerStatus=_EsiServerStatus_Object((1,3,6,1,4,1,14823,2,2,1,10,1,1,1,10),_EsiServerStatus_Type())
esiServerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:esiServerStatus.setStatus(_A)
_EsiServerTrustedModule_Type=Integer32
_EsiServerTrustedModule_Object=MibTableColumn
esiServerTrustedModule=_EsiServerTrustedModule_Object((1,3,6,1,4,1,14823,2,2,1,10,1,1,1,11),_EsiServerTrustedModule_Type())
esiServerTrustedModule.setMaxAccess(_B)
if mibBuilder.loadTexts:esiServerTrustedModule.setStatus(_A)
_EsiServerUntrustedModule_Type=Integer32
_EsiServerUntrustedModule_Object=MibTableColumn
esiServerUntrustedModule=_EsiServerUntrustedModule_Object((1,3,6,1,4,1,14823,2,2,1,10,1,1,1,12),_EsiServerUntrustedModule_Type())
esiServerUntrustedModule.setMaxAccess(_B)
if mibBuilder.loadTexts:esiServerUntrustedModule.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'wlsxESIMIB':wlsxESIMIB,'wlsxESIConfigGroup':wlsxESIConfigGroup,'wlsxESIServerTable':wlsxESIServerTable,'wlsxESIServerEntry':wlsxESIServerEntry,_D:esiServerName,'esiServerGroup':esiServerGroup,'esiServerMode':esiServerMode,'esiServerTrustedIP':esiServerTrustedIP,'esiServerUntrustedIP':esiServerUntrustedIP,'esiServerTrustedSlot':esiServerTrustedSlot,'esiServerTrustedPort':esiServerTrustedPort,'esiServerUntrustedSlot':esiServerUntrustedSlot,'esiServerUntrustedPort':esiServerUntrustedPort,'esiServerStatus':esiServerStatus,'esiServerTrustedModule':esiServerTrustedModule,'esiServerUntrustedModule':esiServerUntrustedModule})