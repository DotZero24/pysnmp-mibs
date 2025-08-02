_G='read-only'
_F='TruthValue'
_E='Unsigned32'
_D='jnxVplsPwBindIndex'
_C='jnxVplsConfigIndex'
_B='VPLS-GENERIC-DRAFT-01-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
jnxExperiment,=mibBuilder.importSymbols('JUNIPER-SMI','jnxExperiment')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,transmission=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso','transmission')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','StorageType','TextualConvention',_F)
jnxVplsConfigIndex,jnxVplsPwBindIndex=mibBuilder.importSymbols(_B,_C,_D)
jnxVplsLdpDraft01MIB=ModuleIdentity((1,3,6,1,4,1,2636,5,9))
if mibBuilder.loadTexts:jnxVplsLdpDraft01MIB.setRevisions(('2006-08-30 12:00',))
_JnxVplsLdpNotifications_ObjectIdentity=ObjectIdentity
jnxVplsLdpNotifications=_JnxVplsLdpNotifications_ObjectIdentity((1,3,6,1,4,1,2636,5,9,0))
_JnxVplsLdpObjects_ObjectIdentity=ObjectIdentity
jnxVplsLdpObjects=_JnxVplsLdpObjects_ObjectIdentity((1,3,6,1,4,1,2636,5,9,1))
_JnxVplsLdpConfigTable_Object=MibTable
jnxVplsLdpConfigTable=_JnxVplsLdpConfigTable_Object((1,3,6,1,4,1,2636,5,9,1,1))
if mibBuilder.loadTexts:jnxVplsLdpConfigTable.setStatus(_A)
_JnxVplsLdpConfigEntry_Object=MibTableRow
jnxVplsLdpConfigEntry=_JnxVplsLdpConfigEntry_Object((1,3,6,1,4,1,2636,5,9,1,1,1))
jnxVplsLdpConfigEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:jnxVplsLdpConfigEntry.setStatus(_A)
class _JnxVplsLdpConfigMacAddrWithdraw_Type(TruthValue):defaultValue=1
_JnxVplsLdpConfigMacAddrWithdraw_Type.__name__=_F
_JnxVplsLdpConfigMacAddrWithdraw_Object=MibTableColumn
jnxVplsLdpConfigMacAddrWithdraw=_JnxVplsLdpConfigMacAddrWithdraw_Object((1,3,6,1,4,1,2636,5,9,1,1,1,1),_JnxVplsLdpConfigMacAddrWithdraw_Type())
jnxVplsLdpConfigMacAddrWithdraw.setMaxAccess(_G)
if mibBuilder.loadTexts:jnxVplsLdpConfigMacAddrWithdraw.setStatus(_A)
_JnxVplsLdpPwBindTable_Object=MibTable
jnxVplsLdpPwBindTable=_JnxVplsLdpPwBindTable_Object((1,3,6,1,4,1,2636,5,9,1,2))
if mibBuilder.loadTexts:jnxVplsLdpPwBindTable.setStatus(_A)
_JnxVplsLdpPwBindEntry_Object=MibTableRow
jnxVplsLdpPwBindEntry=_JnxVplsLdpPwBindEntry_Object((1,3,6,1,4,1,2636,5,9,1,2,1))
jnxVplsLdpPwBindEntry.setIndexNames((0,_B,_C),(0,_B,_D))
if mibBuilder.loadTexts:jnxVplsLdpPwBindEntry.setStatus(_A)
class _JnxVplsLdpPwBindMacAddressLimit_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_JnxVplsLdpPwBindMacAddressLimit_Type.__name__=_E
_JnxVplsLdpPwBindMacAddressLimit_Object=MibTableColumn
jnxVplsLdpPwBindMacAddressLimit=_JnxVplsLdpPwBindMacAddressLimit_Object((1,3,6,1,4,1,2636,5,9,1,2,1,1),_JnxVplsLdpPwBindMacAddressLimit_Type())
jnxVplsLdpPwBindMacAddressLimit.setMaxAccess(_G)
if mibBuilder.loadTexts:jnxVplsLdpPwBindMacAddressLimit.setStatus(_A)
_JnxVplsLdpConformance_ObjectIdentity=ObjectIdentity
jnxVplsLdpConformance=_JnxVplsLdpConformance_ObjectIdentity((1,3,6,1,4,1,2636,5,9,2))
jnxVplsLdpPwBindMacTableFull=NotificationType((1,3,6,1,4,1,2636,5,9,0,1))
jnxVplsLdpPwBindMacTableFull.setObjects(*((_B,_C),(_B,_D)))
if mibBuilder.loadTexts:jnxVplsLdpPwBindMacTableFull.setStatus(_A)
mibBuilder.exportSymbols('VPLS-LDP-DRAFT-01-MIB',**{'jnxVplsLdpDraft01MIB':jnxVplsLdpDraft01MIB,'jnxVplsLdpNotifications':jnxVplsLdpNotifications,'jnxVplsLdpPwBindMacTableFull':jnxVplsLdpPwBindMacTableFull,'jnxVplsLdpObjects':jnxVplsLdpObjects,'jnxVplsLdpConfigTable':jnxVplsLdpConfigTable,'jnxVplsLdpConfigEntry':jnxVplsLdpConfigEntry,'jnxVplsLdpConfigMacAddrWithdraw':jnxVplsLdpConfigMacAddrWithdraw,'jnxVplsLdpPwBindTable':jnxVplsLdpPwBindTable,'jnxVplsLdpPwBindEntry':jnxVplsLdpPwBindEntry,'jnxVplsLdpPwBindMacAddressLimit':jnxVplsLdpPwBindMacAddressLimit,'jnxVplsLdpConformance':jnxVplsLdpConformance})