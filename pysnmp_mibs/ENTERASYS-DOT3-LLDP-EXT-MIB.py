_M='etsysDot3LldpExtEeePortGroup'
_L='etsysDot3LldpExtEeeLocFbTwSys'
_K='etsysDot3LldpExtEeeLocRxTwSys'
_J='etsysDot3LldpExtEeeTLVTxEnable'
_I='etsysDot3LldpExtEeeOperStatus'
_H='etsysDot3LldpExtEeeAdminStatus'
_G='Integer32'
_F='lldpV2LocPortIfIndex'
_E='LLDP-V2-MIB'
_D='EnabledStatus'
_C='read-write'
_B='ENTERASYS-DOT3-LLDP-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
lldpV2LocPortIfIndex,=mibBuilder.importSymbols(_E,_F)
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
etsysDot3LldpExtMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,104))
if mibBuilder.loadTexts:etsysDot3LldpExtMIB.setRevisions(('2013-08-28 17:51',))
_EtsysDot3LldpExtObjects_ObjectIdentity=ObjectIdentity
etsysDot3LldpExtObjects=_EtsysDot3LldpExtObjects_ObjectIdentity((1,3,6,1,4,1,5624,1,2,104,1))
_EtsysDot3LldpExtEeePort_ObjectIdentity=ObjectIdentity
etsysDot3LldpExtEeePort=_EtsysDot3LldpExtEeePort_ObjectIdentity((1,3,6,1,4,1,5624,1,2,104,1,2))
_EtsysDot3LldpExtEeeConfigTable_Object=MibTable
etsysDot3LldpExtEeeConfigTable=_EtsysDot3LldpExtEeeConfigTable_Object((1,3,6,1,4,1,5624,1,2,104,1,2,1))
if mibBuilder.loadTexts:etsysDot3LldpExtEeeConfigTable.setStatus(_A)
_EtsysDot3LldpExtEeeConfigEntry_Object=MibTableRow
etsysDot3LldpExtEeeConfigEntry=_EtsysDot3LldpExtEeeConfigEntry_Object((1,3,6,1,4,1,5624,1,2,104,1,2,1,1))
etsysDot3LldpExtEeeConfigEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:etsysDot3LldpExtEeeConfigEntry.setStatus(_A)
class _EtsysDot3LldpExtEeeAdminStatus_Type(EnabledStatus):defaultValue=2
_EtsysDot3LldpExtEeeAdminStatus_Type.__name__=_D
_EtsysDot3LldpExtEeeAdminStatus_Object=MibTableColumn
etsysDot3LldpExtEeeAdminStatus=_EtsysDot3LldpExtEeeAdminStatus_Object((1,3,6,1,4,1,5624,1,2,104,1,2,1,1,1),_EtsysDot3LldpExtEeeAdminStatus_Type())
etsysDot3LldpExtEeeAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot3LldpExtEeeAdminStatus.setStatus(_A)
class _EtsysDot3LldpExtEeeOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('enabled',1),('disabled',2),('unsupported',3)))
_EtsysDot3LldpExtEeeOperStatus_Type.__name__=_G
_EtsysDot3LldpExtEeeOperStatus_Object=MibTableColumn
etsysDot3LldpExtEeeOperStatus=_EtsysDot3LldpExtEeeOperStatus_Object((1,3,6,1,4,1,5624,1,2,104,1,2,1,1,2),_EtsysDot3LldpExtEeeOperStatus_Type())
etsysDot3LldpExtEeeOperStatus.setMaxAccess('read-only')
if mibBuilder.loadTexts:etsysDot3LldpExtEeeOperStatus.setStatus(_A)
class _EtsysDot3LldpExtEeeTLVTxEnable_Type(EnabledStatus):defaultValue=2
_EtsysDot3LldpExtEeeTLVTxEnable_Type.__name__=_D
_EtsysDot3LldpExtEeeTLVTxEnable_Object=MibTableColumn
etsysDot3LldpExtEeeTLVTxEnable=_EtsysDot3LldpExtEeeTLVTxEnable_Object((1,3,6,1,4,1,5624,1,2,104,1,2,1,1,3),_EtsysDot3LldpExtEeeTLVTxEnable_Type())
etsysDot3LldpExtEeeTLVTxEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot3LldpExtEeeTLVTxEnable.setStatus(_A)
_EtsysDot3LldpExtEeeLocRxTwSys_Type=Integer32
_EtsysDot3LldpExtEeeLocRxTwSys_Object=MibTableColumn
etsysDot3LldpExtEeeLocRxTwSys=_EtsysDot3LldpExtEeeLocRxTwSys_Object((1,3,6,1,4,1,5624,1,2,104,1,2,1,1,4),_EtsysDot3LldpExtEeeLocRxTwSys_Type())
etsysDot3LldpExtEeeLocRxTwSys.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot3LldpExtEeeLocRxTwSys.setStatus(_A)
_EtsysDot3LldpExtEeeLocFbTwSys_Type=Integer32
_EtsysDot3LldpExtEeeLocFbTwSys_Object=MibTableColumn
etsysDot3LldpExtEeeLocFbTwSys=_EtsysDot3LldpExtEeeLocFbTwSys_Object((1,3,6,1,4,1,5624,1,2,104,1,2,1,1,5),_EtsysDot3LldpExtEeeLocFbTwSys_Type())
etsysDot3LldpExtEeeLocFbTwSys.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot3LldpExtEeeLocFbTwSys.setStatus(_A)
_EtsysDot3LldpExtConformance_ObjectIdentity=ObjectIdentity
etsysDot3LldpExtConformance=_EtsysDot3LldpExtConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,104,2))
_EtsysDot3LldpExtGroups_ObjectIdentity=ObjectIdentity
etsysDot3LldpExtGroups=_EtsysDot3LldpExtGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,104,2,1))
_EtsysDot3LldpExtCompliances_ObjectIdentity=ObjectIdentity
etsysDot3LldpExtCompliances=_EtsysDot3LldpExtCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,104,2,2))
etsysDot3LldpExtEeePortGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,104,2,1,1))
etsysDot3LldpExtEeePortGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:etsysDot3LldpExtEeePortGroup.setStatus(_A)
etsysDot3LldpExtEeePortCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,104,2,2,1))
etsysDot3LldpExtEeePortCompliance.setObjects((_B,_M))
if mibBuilder.loadTexts:etsysDot3LldpExtEeePortCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'etsysDot3LldpExtMIB':etsysDot3LldpExtMIB,'etsysDot3LldpExtObjects':etsysDot3LldpExtObjects,'etsysDot3LldpExtEeePort':etsysDot3LldpExtEeePort,'etsysDot3LldpExtEeeConfigTable':etsysDot3LldpExtEeeConfigTable,'etsysDot3LldpExtEeeConfigEntry':etsysDot3LldpExtEeeConfigEntry,_H:etsysDot3LldpExtEeeAdminStatus,_I:etsysDot3LldpExtEeeOperStatus,_J:etsysDot3LldpExtEeeTLVTxEnable,_K:etsysDot3LldpExtEeeLocRxTwSys,_L:etsysDot3LldpExtEeeLocFbTwSys,'etsysDot3LldpExtConformance':etsysDot3LldpExtConformance,'etsysDot3LldpExtGroups':etsysDot3LldpExtGroups,_M:etsysDot3LldpExtEeePortGroup,'etsysDot3LldpExtCompliances':etsysDot3LldpExtCompliances,'etsysDot3LldpExtEeePortCompliance':etsysDot3LldpExtEeePortCompliance})