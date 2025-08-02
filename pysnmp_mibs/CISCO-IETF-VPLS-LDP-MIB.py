_K='cvplsLdpPwBindMacAddressLimit'
_J='cvplsLdpConfigMacAddrWithdraw'
_I='read-create'
_H='TruthValue'
_G='Unsigned32'
_F='cvplsPwBindIndex'
_E='cvplsLdpGroup'
_D='cvplsConfigIndex'
_C='CISCO-IETF-VPLS-GENERIC-MIB'
_B='CISCO-IETF-VPLS-LDP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cvplsConfigIndex,cvplsPwBindIndex=mibBuilder.importSymbols(_C,_D,_F)
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_H)
VPNId,=mibBuilder.importSymbols('VPN-TC-STD-MIB','VPNId')
cvplsLdpMIB=ModuleIdentity((1,3,6,1,4,1,9,10,141))
if mibBuilder.loadTexts:cvplsLdpMIB.setRevisions(('2007-11-22 12:00',))
_CvplsLdpObjects_ObjectIdentity=ObjectIdentity
cvplsLdpObjects=_CvplsLdpObjects_ObjectIdentity((1,3,6,1,4,1,9,10,141,1))
_CvplsLdpConfigTable_Object=MibTable
cvplsLdpConfigTable=_CvplsLdpConfigTable_Object((1,3,6,1,4,1,9,10,141,1,1))
if mibBuilder.loadTexts:cvplsLdpConfigTable.setStatus(_A)
_CvplsLdpConfigEntry_Object=MibTableRow
cvplsLdpConfigEntry=_CvplsLdpConfigEntry_Object((1,3,6,1,4,1,9,10,141,1,1,1))
cvplsLdpConfigEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:cvplsLdpConfigEntry.setStatus(_A)
class _CvplsLdpConfigMacAddrWithdraw_Type(TruthValue):defaultValue=1
_CvplsLdpConfigMacAddrWithdraw_Type.__name__=_H
_CvplsLdpConfigMacAddrWithdraw_Object=MibTableColumn
cvplsLdpConfigMacAddrWithdraw=_CvplsLdpConfigMacAddrWithdraw_Object((1,3,6,1,4,1,9,10,141,1,1,1,1),_CvplsLdpConfigMacAddrWithdraw_Type())
cvplsLdpConfigMacAddrWithdraw.setMaxAccess(_I)
if mibBuilder.loadTexts:cvplsLdpConfigMacAddrWithdraw.setStatus(_A)
_CvplsLdpPwBindTable_Object=MibTable
cvplsLdpPwBindTable=_CvplsLdpPwBindTable_Object((1,3,6,1,4,1,9,10,141,1,2))
if mibBuilder.loadTexts:cvplsLdpPwBindTable.setStatus(_A)
_CvplsLdpPwBindEntry_Object=MibTableRow
cvplsLdpPwBindEntry=_CvplsLdpPwBindEntry_Object((1,3,6,1,4,1,9,10,141,1,2,1))
cvplsLdpPwBindEntry.setIndexNames((0,_C,_D),(0,_C,_F))
if mibBuilder.loadTexts:cvplsLdpPwBindEntry.setStatus(_A)
class _CvplsLdpPwBindMacAddressLimit_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CvplsLdpPwBindMacAddressLimit_Type.__name__=_G
_CvplsLdpPwBindMacAddressLimit_Object=MibTableColumn
cvplsLdpPwBindMacAddressLimit=_CvplsLdpPwBindMacAddressLimit_Object((1,3,6,1,4,1,9,10,141,1,2,1,1),_CvplsLdpPwBindMacAddressLimit_Type())
cvplsLdpPwBindMacAddressLimit.setMaxAccess(_I)
if mibBuilder.loadTexts:cvplsLdpPwBindMacAddressLimit.setStatus(_A)
_CvplsLdpConformance_ObjectIdentity=ObjectIdentity
cvplsLdpConformance=_CvplsLdpConformance_ObjectIdentity((1,3,6,1,4,1,9,10,141,2))
_CvplsLdpCompliances_ObjectIdentity=ObjectIdentity
cvplsLdpCompliances=_CvplsLdpCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,141,2,1))
_CvplsLdpGroups_ObjectIdentity=ObjectIdentity
cvplsLdpGroups=_CvplsLdpGroups_ObjectIdentity((1,3,6,1,4,1,9,10,141,2,2))
cvplsLdpGroup=ObjectGroup((1,3,6,1,4,1,9,10,141,2,2,1))
cvplsLdpGroup.setObjects(*((_B,_J),(_B,_K)))
if mibBuilder.loadTexts:cvplsLdpGroup.setStatus(_A)
cvplsLdpModuleFullCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,141,2,1,1))
cvplsLdpModuleFullCompliance.setObjects((_B,_E))
if mibBuilder.loadTexts:cvplsLdpModuleFullCompliance.setStatus(_A)
cvplsLdpModuleReadOnlyCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,141,2,1,2))
cvplsLdpModuleReadOnlyCompliance.setObjects((_B,_E))
if mibBuilder.loadTexts:cvplsLdpModuleReadOnlyCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'cvplsLdpMIB':cvplsLdpMIB,'cvplsLdpObjects':cvplsLdpObjects,'cvplsLdpConfigTable':cvplsLdpConfigTable,'cvplsLdpConfigEntry':cvplsLdpConfigEntry,_J:cvplsLdpConfigMacAddrWithdraw,'cvplsLdpPwBindTable':cvplsLdpPwBindTable,'cvplsLdpPwBindEntry':cvplsLdpPwBindEntry,_K:cvplsLdpPwBindMacAddressLimit,'cvplsLdpConformance':cvplsLdpConformance,'cvplsLdpCompliances':cvplsLdpCompliances,'cvplsLdpModuleFullCompliance':cvplsLdpModuleFullCompliance,'cvplsLdpModuleReadOnlyCompliance':cvplsLdpModuleReadOnlyCompliance,'cvplsLdpGroups':cvplsLdpGroups,_E:cvplsLdpGroup})