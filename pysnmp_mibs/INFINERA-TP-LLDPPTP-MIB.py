_O='lldpPtpGroup'
_N='lldpRemoteSysLastReceivedTimeString'
_M='lldpRemoteSysSysDesc'
_L='lldpRemoteSysSysName'
_K='lldpRemoteSysPortDesc'
_J='lldpRemoteSysTtl'
_I='lldpRemoteSysPortId'
_H='lldpRemoteSysPortIdSubtype'
_G='lldpRemoteSysChassisId'
_F='lldpRemoteSysChassisIdSubtype'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='INFINERA-TP-LLDPPTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_D,_E)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
InfnChassisIdSubtype,InfnManAddrIfSubtype,InfnManAddrSubtype,InfnPortIdSubtype=mibBuilder.importSymbols('INFINERA-TC-MIB','InfnChassisIdSubtype','InfnManAddrIfSubtype','InfnManAddrSubtype','InfnPortIdSubtype')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
lldpPtpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,56))
if mibBuilder.loadTexts:lldpPtpMIB.setRevisions(('2015-06-24 00:00',))
_LldpRemoteSysPtpTable_Object=MibTable
lldpRemoteSysPtpTable=_LldpRemoteSysPtpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,56,1))
if mibBuilder.loadTexts:lldpRemoteSysPtpTable.setStatus(_A)
_LldpPtpEntry_Object=MibTableRow
lldpPtpEntry=_LldpPtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,56,1,1))
lldpPtpEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:lldpPtpEntry.setStatus(_A)
_LldpRemoteSysChassisIdSubtype_Type=InfnChassisIdSubtype
_LldpRemoteSysChassisIdSubtype_Object=MibTableColumn
lldpRemoteSysChassisIdSubtype=_LldpRemoteSysChassisIdSubtype_Object((1,3,6,1,4,1,21296,2,2,2,2,56,1,1,1),_LldpRemoteSysChassisIdSubtype_Type())
lldpRemoteSysChassisIdSubtype.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpRemoteSysChassisIdSubtype.setStatus(_A)
_LldpRemoteSysChassisId_Type=DisplayString
_LldpRemoteSysChassisId_Object=MibTableColumn
lldpRemoteSysChassisId=_LldpRemoteSysChassisId_Object((1,3,6,1,4,1,21296,2,2,2,2,56,1,1,2),_LldpRemoteSysChassisId_Type())
lldpRemoteSysChassisId.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpRemoteSysChassisId.setStatus(_A)
_LldpRemoteSysPortIdSubtype_Type=InfnPortIdSubtype
_LldpRemoteSysPortIdSubtype_Object=MibTableColumn
lldpRemoteSysPortIdSubtype=_LldpRemoteSysPortIdSubtype_Object((1,3,6,1,4,1,21296,2,2,2,2,56,1,1,3),_LldpRemoteSysPortIdSubtype_Type())
lldpRemoteSysPortIdSubtype.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpRemoteSysPortIdSubtype.setStatus(_A)
_LldpRemoteSysPortId_Type=DisplayString
_LldpRemoteSysPortId_Object=MibTableColumn
lldpRemoteSysPortId=_LldpRemoteSysPortId_Object((1,3,6,1,4,1,21296,2,2,2,2,56,1,1,4),_LldpRemoteSysPortId_Type())
lldpRemoteSysPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpRemoteSysPortId.setStatus(_A)
_LldpRemoteSysTtl_Type=Integer32
_LldpRemoteSysTtl_Object=MibTableColumn
lldpRemoteSysTtl=_LldpRemoteSysTtl_Object((1,3,6,1,4,1,21296,2,2,2,2,56,1,1,5),_LldpRemoteSysTtl_Type())
lldpRemoteSysTtl.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpRemoteSysTtl.setStatus(_A)
_LldpRemoteSysPortDesc_Type=DisplayString
_LldpRemoteSysPortDesc_Object=MibTableColumn
lldpRemoteSysPortDesc=_LldpRemoteSysPortDesc_Object((1,3,6,1,4,1,21296,2,2,2,2,56,1,1,6),_LldpRemoteSysPortDesc_Type())
lldpRemoteSysPortDesc.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpRemoteSysPortDesc.setStatus(_A)
_LldpRemoteSysSysName_Type=DisplayString
_LldpRemoteSysSysName_Object=MibTableColumn
lldpRemoteSysSysName=_LldpRemoteSysSysName_Object((1,3,6,1,4,1,21296,2,2,2,2,56,1,1,7),_LldpRemoteSysSysName_Type())
lldpRemoteSysSysName.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpRemoteSysSysName.setStatus(_A)
_LldpRemoteSysSysDesc_Type=DisplayString
_LldpRemoteSysSysDesc_Object=MibTableColumn
lldpRemoteSysSysDesc=_LldpRemoteSysSysDesc_Object((1,3,6,1,4,1,21296,2,2,2,2,56,1,1,8),_LldpRemoteSysSysDesc_Type())
lldpRemoteSysSysDesc.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpRemoteSysSysDesc.setStatus(_A)
_LldpRemoteSysLastReceivedTimeString_Type=DisplayString
_LldpRemoteSysLastReceivedTimeString_Object=MibTableColumn
lldpRemoteSysLastReceivedTimeString=_LldpRemoteSysLastReceivedTimeString_Object((1,3,6,1,4,1,21296,2,2,2,2,56,1,1,9),_LldpRemoteSysLastReceivedTimeString_Type())
lldpRemoteSysLastReceivedTimeString.setMaxAccess('read-write')
if mibBuilder.loadTexts:lldpRemoteSysLastReceivedTimeString.setStatus(_A)
_LldpPtpConformance_ObjectIdentity=ObjectIdentity
lldpPtpConformance=_LldpPtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,56,3))
_LldpPtpCompliances_ObjectIdentity=ObjectIdentity
lldpPtpCompliances=_LldpPtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,56,3,1))
_LldpPtpGroups_ObjectIdentity=ObjectIdentity
lldpPtpGroups=_LldpPtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,56,3,2))
lldpPtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,56,3,2,1))
lldpPtpGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:lldpPtpGroup.setStatus(_A)
lldpPtpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,56,3,1,1))
lldpPtpCompliance.setObjects((_B,_O))
if mibBuilder.loadTexts:lldpPtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'lldpPtpMIB':lldpPtpMIB,'lldpRemoteSysPtpTable':lldpRemoteSysPtpTable,'lldpPtpEntry':lldpPtpEntry,_F:lldpRemoteSysChassisIdSubtype,_G:lldpRemoteSysChassisId,_H:lldpRemoteSysPortIdSubtype,_I:lldpRemoteSysPortId,_J:lldpRemoteSysTtl,_K:lldpRemoteSysPortDesc,_L:lldpRemoteSysSysName,_M:lldpRemoteSysSysDesc,_N:lldpRemoteSysLastReceivedTimeString,'lldpPtpConformance':lldpPtpConformance,'lldpPtpCompliances':lldpPtpCompliances,'lldpPtpCompliance':lldpPtpCompliance,'lldpPtpGroups':lldpPtpGroups,_O:lldpPtpGroup})