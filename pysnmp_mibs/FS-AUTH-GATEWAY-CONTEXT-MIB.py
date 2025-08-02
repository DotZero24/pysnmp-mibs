_L='fsWebAuthVCMIBGroup'
_K='authUserStatusVC'
_J='authUserTimeUsedVC'
_I='authUserTimeLimitVC'
_H='authUserOnlineFlagVC'
_G='read-create'
_F='DisplayString'
_E='authUserIpAddrVC'
_D='authUserContextNameVC'
_C='read-only'
_B='FS-AUTH-GATEWAY-CONTEXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','RowStatus','TextualConvention')
fsWebAuthVCMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,67))
if mibBuilder.loadTexts:fsWebAuthVCMIB.setRevisions(('2009-12-06 00:00',))
_FsWebAuthVCMIBObjects_ObjectIdentity=ObjectIdentity
fsWebAuthVCMIBObjects=_FsWebAuthVCMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,67,1))
_FsWebAuthUserVCTable_Object=MibTable
fsWebAuthUserVCTable=_FsWebAuthUserVCTable_Object((1,3,6,1,4,1,52642,1,1,10,2,67,1,1))
if mibBuilder.loadTexts:fsWebAuthUserVCTable.setStatus(_A)
_FsWebAuthUserVCEntry_Object=MibTableRow
fsWebAuthUserVCEntry=_FsWebAuthUserVCEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,67,1,1,1))
fsWebAuthUserVCEntry.setIndexNames((0,_B,_D),(0,_B,_E))
if mibBuilder.loadTexts:fsWebAuthUserVCEntry.setStatus(_A)
class _AuthUserContextNameVC_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_AuthUserContextNameVC_Type.__name__=_F
_AuthUserContextNameVC_Object=MibTableColumn
authUserContextNameVC=_AuthUserContextNameVC_Object((1,3,6,1,4,1,52642,1,1,10,2,67,1,1,1,1),_AuthUserContextNameVC_Type())
authUserContextNameVC.setMaxAccess(_C)
if mibBuilder.loadTexts:authUserContextNameVC.setStatus(_A)
_AuthUserIpAddrVC_Type=IpAddress
_AuthUserIpAddrVC_Object=MibTableColumn
authUserIpAddrVC=_AuthUserIpAddrVC_Object((1,3,6,1,4,1,52642,1,1,10,2,67,1,1,1,2),_AuthUserIpAddrVC_Type())
authUserIpAddrVC.setMaxAccess(_C)
if mibBuilder.loadTexts:authUserIpAddrVC.setStatus(_A)
_AuthUserOnlineFlagVC_Type=Gauge32
_AuthUserOnlineFlagVC_Object=MibTableColumn
authUserOnlineFlagVC=_AuthUserOnlineFlagVC_Object((1,3,6,1,4,1,52642,1,1,10,2,67,1,1,1,3),_AuthUserOnlineFlagVC_Type())
authUserOnlineFlagVC.setMaxAccess(_C)
if mibBuilder.loadTexts:authUserOnlineFlagVC.setStatus(_A)
_AuthUserTimeLimitVC_Type=Gauge32
_AuthUserTimeLimitVC_Object=MibTableColumn
authUserTimeLimitVC=_AuthUserTimeLimitVC_Object((1,3,6,1,4,1,52642,1,1,10,2,67,1,1,1,4),_AuthUserTimeLimitVC_Type())
authUserTimeLimitVC.setMaxAccess(_G)
if mibBuilder.loadTexts:authUserTimeLimitVC.setStatus(_A)
_AuthUserTimeUsedVC_Type=Gauge32
_AuthUserTimeUsedVC_Object=MibTableColumn
authUserTimeUsedVC=_AuthUserTimeUsedVC_Object((1,3,6,1,4,1,52642,1,1,10,2,67,1,1,1,5),_AuthUserTimeUsedVC_Type())
authUserTimeUsedVC.setMaxAccess(_C)
if mibBuilder.loadTexts:authUserTimeUsedVC.setStatus(_A)
_AuthUserStatusVC_Type=RowStatus
_AuthUserStatusVC_Object=MibTableColumn
authUserStatusVC=_AuthUserStatusVC_Object((1,3,6,1,4,1,52642,1,1,10,2,67,1,1,1,6),_AuthUserStatusVC_Type())
authUserStatusVC.setMaxAccess(_G)
if mibBuilder.loadTexts:authUserStatusVC.setStatus(_A)
_FsWebAuthVCMIBConformance_ObjectIdentity=ObjectIdentity
fsWebAuthVCMIBConformance=_FsWebAuthVCMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,67,3))
_FsWebAuthVCMIBCompliances_ObjectIdentity=ObjectIdentity
fsWebAuthVCMIBCompliances=_FsWebAuthVCMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,67,3,1))
_FsWebAuthVCMIBGroups_ObjectIdentity=ObjectIdentity
fsWebAuthVCMIBGroups=_FsWebAuthVCMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,67,3,2))
fsWebAuthVCMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,67,3,2,1))
fsWebAuthVCMIBGroup.setObjects(*((_B,_D),(_B,_E),(_B,_H),(_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:fsWebAuthVCMIBGroup.setStatus(_A)
fsWebAuthVCMIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,67,3,1,1))
fsWebAuthVCMIBCompliance.setObjects((_B,_L))
if mibBuilder.loadTexts:fsWebAuthVCMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fsWebAuthVCMIB':fsWebAuthVCMIB,'fsWebAuthVCMIBObjects':fsWebAuthVCMIBObjects,'fsWebAuthUserVCTable':fsWebAuthUserVCTable,'fsWebAuthUserVCEntry':fsWebAuthUserVCEntry,_D:authUserContextNameVC,_E:authUserIpAddrVC,_H:authUserOnlineFlagVC,_I:authUserTimeLimitVC,_J:authUserTimeUsedVC,_K:authUserStatusVC,'fsWebAuthVCMIBConformance':fsWebAuthVCMIBConformance,'fsWebAuthVCMIBCompliances':fsWebAuthVCMIBCompliances,'fsWebAuthVCMIBCompliance':fsWebAuthVCMIBCompliance,'fsWebAuthVCMIBGroups':fsWebAuthVCMIBGroups,_L:fsWebAuthVCMIBGroup})