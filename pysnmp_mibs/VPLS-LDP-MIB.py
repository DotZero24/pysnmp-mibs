_O='vplsLdpPwBindMacTableFull'
_N='vplsLdpPwBindMacAddressLimit'
_M='vplsLdpConfigMacAddrWithdraw'
_L='read-write'
_K='vplsConfigName'
_J='TruthValue'
_I='Unsigned32'
_H='pwIndex'
_G='vplsLdpNotificationGroup'
_F='vplsLdpGroup'
_E='vplsConfigIndex'
_D='PW-STD-MIB'
_C='VPLS-GENERIC-MIB'
_B='VPLS-LDP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
pwID,pwIndex=mibBuilder.importSymbols(_D,'pwID',_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,transmission=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso','transmission')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_J)
vplsConfigIndex,vplsConfigName=mibBuilder.importSymbols(_C,_E,_K)
vplsLdpMIB=ModuleIdentity((1,3,6,1,2,1,10,275))
if mibBuilder.loadTexts:vplsLdpMIB.setRevisions(('2014-05-19 12:00',))
_VplsLdpNotifications_ObjectIdentity=ObjectIdentity
vplsLdpNotifications=_VplsLdpNotifications_ObjectIdentity((1,3,6,1,2,1,10,275,0))
_VplsLdpObjects_ObjectIdentity=ObjectIdentity
vplsLdpObjects=_VplsLdpObjects_ObjectIdentity((1,3,6,1,2,1,10,275,1))
_VplsLdpConfigTable_Object=MibTable
vplsLdpConfigTable=_VplsLdpConfigTable_Object((1,3,6,1,2,1,10,275,1,1))
if mibBuilder.loadTexts:vplsLdpConfigTable.setStatus(_A)
_VplsLdpConfigEntry_Object=MibTableRow
vplsLdpConfigEntry=_VplsLdpConfigEntry_Object((1,3,6,1,2,1,10,275,1,1,1))
vplsLdpConfigEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:vplsLdpConfigEntry.setStatus(_A)
class _VplsLdpConfigMacAddrWithdraw_Type(TruthValue):defaultValue=1
_VplsLdpConfigMacAddrWithdraw_Type.__name__=_J
_VplsLdpConfigMacAddrWithdraw_Object=MibTableColumn
vplsLdpConfigMacAddrWithdraw=_VplsLdpConfigMacAddrWithdraw_Object((1,3,6,1,2,1,10,275,1,1,1,1),_VplsLdpConfigMacAddrWithdraw_Type())
vplsLdpConfigMacAddrWithdraw.setMaxAccess(_L)
if mibBuilder.loadTexts:vplsLdpConfigMacAddrWithdraw.setStatus(_A)
_VplsLdpPwBindTable_Object=MibTable
vplsLdpPwBindTable=_VplsLdpPwBindTable_Object((1,3,6,1,2,1,10,275,1,2))
if mibBuilder.loadTexts:vplsLdpPwBindTable.setStatus(_A)
_VplsLdpPwBindEntry_Object=MibTableRow
vplsLdpPwBindEntry=_VplsLdpPwBindEntry_Object((1,3,6,1,2,1,10,275,1,2,1))
vplsLdpPwBindEntry.setIndexNames((0,_C,_E),(0,_D,_H))
if mibBuilder.loadTexts:vplsLdpPwBindEntry.setStatus(_A)
class _VplsLdpPwBindMacAddressLimit_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_VplsLdpPwBindMacAddressLimit_Type.__name__=_I
_VplsLdpPwBindMacAddressLimit_Object=MibTableColumn
vplsLdpPwBindMacAddressLimit=_VplsLdpPwBindMacAddressLimit_Object((1,3,6,1,2,1,10,275,1,2,1,1),_VplsLdpPwBindMacAddressLimit_Type())
vplsLdpPwBindMacAddressLimit.setMaxAccess(_L)
if mibBuilder.loadTexts:vplsLdpPwBindMacAddressLimit.setStatus(_A)
_VplsLdpConformance_ObjectIdentity=ObjectIdentity
vplsLdpConformance=_VplsLdpConformance_ObjectIdentity((1,3,6,1,2,1,10,275,2))
_VplsLdpCompliances_ObjectIdentity=ObjectIdentity
vplsLdpCompliances=_VplsLdpCompliances_ObjectIdentity((1,3,6,1,2,1,10,275,2,1))
_VplsLdpGroups_ObjectIdentity=ObjectIdentity
vplsLdpGroups=_VplsLdpGroups_ObjectIdentity((1,3,6,1,2,1,10,275,2,2))
vplsLdpGroup=ObjectGroup((1,3,6,1,2,1,10,275,2,2,1))
vplsLdpGroup.setObjects(*((_B,_M),(_B,_N)))
if mibBuilder.loadTexts:vplsLdpGroup.setStatus(_A)
vplsLdpPwBindMacTableFull=NotificationType((1,3,6,1,2,1,10,275,0,1))
vplsLdpPwBindMacTableFull.setObjects(*((_C,_K),(_D,'pwID')))
if mibBuilder.loadTexts:vplsLdpPwBindMacTableFull.setStatus(_A)
vplsLdpNotificationGroup=NotificationGroup((1,3,6,1,2,1,10,275,2,2,2))
vplsLdpNotificationGroup.setObjects((_B,_O))
if mibBuilder.loadTexts:vplsLdpNotificationGroup.setStatus(_A)
vplsLdpModuleFullCompliance=ModuleCompliance((1,3,6,1,2,1,10,275,2,1,1))
vplsLdpModuleFullCompliance.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:vplsLdpModuleFullCompliance.setStatus(_A)
vplsLdpModuleReadOnlyCompliance=ModuleCompliance((1,3,6,1,2,1,10,275,2,1,2))
vplsLdpModuleReadOnlyCompliance.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:vplsLdpModuleReadOnlyCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'vplsLdpMIB':vplsLdpMIB,'vplsLdpNotifications':vplsLdpNotifications,_O:vplsLdpPwBindMacTableFull,'vplsLdpObjects':vplsLdpObjects,'vplsLdpConfigTable':vplsLdpConfigTable,'vplsLdpConfigEntry':vplsLdpConfigEntry,_M:vplsLdpConfigMacAddrWithdraw,'vplsLdpPwBindTable':vplsLdpPwBindTable,'vplsLdpPwBindEntry':vplsLdpPwBindEntry,_N:vplsLdpPwBindMacAddressLimit,'vplsLdpConformance':vplsLdpConformance,'vplsLdpCompliances':vplsLdpCompliances,'vplsLdpModuleFullCompliance':vplsLdpModuleFullCompliance,'vplsLdpModuleReadOnlyCompliance':vplsLdpModuleReadOnlyCompliance,'vplsLdpGroups':vplsLdpGroups,_F:vplsLdpGroup,_G:vplsLdpNotificationGroup})