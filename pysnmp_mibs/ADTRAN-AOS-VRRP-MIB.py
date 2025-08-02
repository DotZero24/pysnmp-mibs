_S='adGenAOSVrrpNotificationGroup'
_R='adGenAOSVrrpTrapGroup'
_Q='adGenAOSVrrpTrapCfgGroup'
_P='adGenAOSVrrpMasterTrap'
_O='adGenAOSVrrpMasterTrapCntl'
_N='adGenAOSVrrpPriority'
_M='adGenAOSVrrpInetAddr'
_L='adGenAOSVrrpInetAddrType'
_K='adGenAOSVrrpId'
_J='adGenAOSVrrpVersion'
_I='ifIndex'
_H='IF-MIB'
_G='adGenAOSVrrpObjectGroup'
_F='adGenAOSVrrpOperStatus'
_E='read-only'
_D='not-accessible'
_C='Integer32'
_B='ADTRAN-AOS-VRRP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenAOSConformance,adGenAOSRouter=mibBuilder.importSymbols('ADTRAN-AOS','adGenAOSConformance','adGenAOSRouter')
adIdentity,=mibBuilder.importSymbols('ADTRAN-MIB','adIdentity')
ifIndex,=mibBuilder.importSymbols(_H,_I)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adGenAOSVrrpMib=ModuleIdentity((1,3,6,1,4,1,664,6,10000,53,2,3))
if mibBuilder.loadTexts:adGenAOSVrrpMib.setRevisions(('2014-07-29 00:00','2014-04-17 00:00'))
_AdGenAOSVrrp_ObjectIdentity=ObjectIdentity
adGenAOSVrrp=_AdGenAOSVrrp_ObjectIdentity((1,3,6,1,4,1,664,5,53,2,3))
_AdGenAOSVrrpTrap_ObjectIdentity=ObjectIdentity
adGenAOSVrrpTrap=_AdGenAOSVrrpTrap_ObjectIdentity((1,3,6,1,4,1,664,5,53,2,3,0))
_AdGenAOSVrrpTrapCntl_ObjectIdentity=ObjectIdentity
adGenAOSVrrpTrapCntl=_AdGenAOSVrrpTrapCntl_ObjectIdentity((1,3,6,1,4,1,664,5,53,2,3,1))
class _AdGenAOSVrrpMasterTrapCntl_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_AdGenAOSVrrpMasterTrapCntl_Type.__name__=_C
_AdGenAOSVrrpMasterTrapCntl_Object=MibScalar
adGenAOSVrrpMasterTrapCntl=_AdGenAOSVrrpMasterTrapCntl_Object((1,3,6,1,4,1,664,5,53,2,3,1,1),_AdGenAOSVrrpMasterTrapCntl_Type())
adGenAOSVrrpMasterTrapCntl.setMaxAccess('read-write')
if mibBuilder.loadTexts:adGenAOSVrrpMasterTrapCntl.setStatus(_A)
_AdGenAOSVrrpTable_Object=MibTable
adGenAOSVrrpTable=_AdGenAOSVrrpTable_Object((1,3,6,1,4,1,664,5,53,2,3,2))
if mibBuilder.loadTexts:adGenAOSVrrpTable.setStatus(_A)
_AdGenAOSVrrpEntry_Object=MibTableRow
adGenAOSVrrpEntry=_AdGenAOSVrrpEntry_Object((1,3,6,1,4,1,664,5,53,2,3,2,1))
adGenAOSVrrpEntry.setIndexNames((0,_H,_I),(0,_B,_J),(0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:adGenAOSVrrpEntry.setStatus(_A)
class _AdGenAOSVrrpVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('v2',2),('v3',3)))
_AdGenAOSVrrpVersion_Type.__name__=_C
_AdGenAOSVrrpVersion_Object=MibTableColumn
adGenAOSVrrpVersion=_AdGenAOSVrrpVersion_Object((1,3,6,1,4,1,664,5,53,2,3,2,1,1),_AdGenAOSVrrpVersion_Type())
adGenAOSVrrpVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenAOSVrrpVersion.setStatus(_A)
class _AdGenAOSVrrpId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AdGenAOSVrrpId_Type.__name__=_C
_AdGenAOSVrrpId_Object=MibTableColumn
adGenAOSVrrpId=_AdGenAOSVrrpId_Object((1,3,6,1,4,1,664,5,53,2,3,2,1,2),_AdGenAOSVrrpId_Type())
adGenAOSVrrpId.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenAOSVrrpId.setStatus(_A)
_AdGenAOSVrrpInetAddrType_Type=InetAddressType
_AdGenAOSVrrpInetAddrType_Object=MibTableColumn
adGenAOSVrrpInetAddrType=_AdGenAOSVrrpInetAddrType_Object((1,3,6,1,4,1,664,5,53,2,3,2,1,3),_AdGenAOSVrrpInetAddrType_Type())
adGenAOSVrrpInetAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenAOSVrrpInetAddrType.setStatus(_A)
_AdGenAOSVrrpInetAddr_Type=InetAddress
_AdGenAOSVrrpInetAddr_Object=MibTableColumn
adGenAOSVrrpInetAddr=_AdGenAOSVrrpInetAddr_Object((1,3,6,1,4,1,664,5,53,2,3,2,1,4),_AdGenAOSVrrpInetAddr_Type())
adGenAOSVrrpInetAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:adGenAOSVrrpInetAddr.setStatus(_A)
class _AdGenAOSVrrpOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('initialize',1),('backup',2),('master',3)))
_AdGenAOSVrrpOperStatus_Type.__name__=_C
_AdGenAOSVrrpOperStatus_Object=MibTableColumn
adGenAOSVrrpOperStatus=_AdGenAOSVrrpOperStatus_Object((1,3,6,1,4,1,664,5,53,2,3,2,1,5),_AdGenAOSVrrpOperStatus_Type())
adGenAOSVrrpOperStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:adGenAOSVrrpOperStatus.setStatus(_A)
class _AdGenAOSVrrpPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AdGenAOSVrrpPriority_Type.__name__=_C
_AdGenAOSVrrpPriority_Object=MibTableColumn
adGenAOSVrrpPriority=_AdGenAOSVrrpPriority_Object((1,3,6,1,4,1,664,5,53,2,3,2,1,6),_AdGenAOSVrrpPriority_Type())
adGenAOSVrrpPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:adGenAOSVrrpPriority.setStatus(_A)
_AdGenAOSVrrpConformance_ObjectIdentity=ObjectIdentity
adGenAOSVrrpConformance=_AdGenAOSVrrpConformance_ObjectIdentity((1,3,6,1,4,1,664,5,53,99,20))
_AdGenAOSVrrpGroups_ObjectIdentity=ObjectIdentity
adGenAOSVrrpGroups=_AdGenAOSVrrpGroups_ObjectIdentity((1,3,6,1,4,1,664,5,53,99,20,1))
_AdGenAOSVrrpCompliances_ObjectIdentity=ObjectIdentity
adGenAOSVrrpCompliances=_AdGenAOSVrrpCompliances_ObjectIdentity((1,3,6,1,4,1,664,5,53,99,20,2))
adGenAOSVrrpObjectGroup=ObjectGroup((1,3,6,1,4,1,664,5,53,99,20,1,1))
adGenAOSVrrpObjectGroup.setObjects(*((_B,_M),(_B,_N)))
if mibBuilder.loadTexts:adGenAOSVrrpObjectGroup.setStatus(_A)
adGenAOSVrrpTrapCfgGroup=ObjectGroup((1,3,6,1,4,1,664,5,53,99,20,1,2))
adGenAOSVrrpTrapCfgGroup.setObjects((_B,_O))
if mibBuilder.loadTexts:adGenAOSVrrpTrapCfgGroup.setStatus(_A)
adGenAOSVrrpTrapGroup=ObjectGroup((1,3,6,1,4,1,664,5,53,99,20,1,3))
adGenAOSVrrpTrapGroup.setObjects((_B,_F))
if mibBuilder.loadTexts:adGenAOSVrrpTrapGroup.setStatus(_A)
adGenAOSVrrpMasterTrap=NotificationType((1,3,6,1,4,1,664,5,53,2,3,0,1))
adGenAOSVrrpMasterTrap.setObjects((_B,_F))
if mibBuilder.loadTexts:adGenAOSVrrpMasterTrap.setStatus(_A)
adGenAOSVrrpNotificationGroup=NotificationGroup((1,3,6,1,4,1,664,5,53,99,20,1,4))
adGenAOSVrrpNotificationGroup.setObjects((_B,_P))
if mibBuilder.loadTexts:adGenAOSVrrpNotificationGroup.setStatus(_A)
adGenAOSVrrpFullCompliance=ModuleCompliance((1,3,6,1,4,1,664,5,53,99,20,2,1))
adGenAOSVrrpFullCompliance.setObjects(*((_B,_G),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:adGenAOSVrrpFullCompliance.setStatus(_A)
adGenAOSVrrpReadOnlyCompliance=ModuleCompliance((1,3,6,1,4,1,664,5,53,99,20,2,2))
adGenAOSVrrpReadOnlyCompliance.setObjects((_B,_G))
if mibBuilder.loadTexts:adGenAOSVrrpReadOnlyCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'adGenAOSVrrp':adGenAOSVrrp,'adGenAOSVrrpTrap':adGenAOSVrrpTrap,_P:adGenAOSVrrpMasterTrap,'adGenAOSVrrpTrapCntl':adGenAOSVrrpTrapCntl,_O:adGenAOSVrrpMasterTrapCntl,'adGenAOSVrrpTable':adGenAOSVrrpTable,'adGenAOSVrrpEntry':adGenAOSVrrpEntry,_J:adGenAOSVrrpVersion,_K:adGenAOSVrrpId,_L:adGenAOSVrrpInetAddrType,_M:adGenAOSVrrpInetAddr,_F:adGenAOSVrrpOperStatus,_N:adGenAOSVrrpPriority,'adGenAOSVrrpConformance':adGenAOSVrrpConformance,'adGenAOSVrrpGroups':adGenAOSVrrpGroups,_G:adGenAOSVrrpObjectGroup,_Q:adGenAOSVrrpTrapCfgGroup,_R:adGenAOSVrrpTrapGroup,_S:adGenAOSVrrpNotificationGroup,'adGenAOSVrrpCompliances':adGenAOSVrrpCompliances,'adGenAOSVrrpFullCompliance':adGenAOSVrrpFullCompliance,'adGenAOSVrrpReadOnlyCompliance':adGenAOSVrrpReadOnlyCompliance,'adGenAOSVrrpMib':adGenAOSVrrpMib})