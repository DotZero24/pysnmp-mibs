_V='juniRadiusAcctProxyGroup'
_U='juniRadiusAuthProxyGroup'
_T='juniRadiusBasicProxyGroup'
_S='juniRadiusAcctProxyCfgClientKey'
_R='juniRadiusAcctProxyCfgRowStatus'
_Q='juniRadiusAcctProxyCfgPortNumber'
_P='juniRadiusAuthProxyCfgClientKey'
_O='juniRadiusAuthProxyCfgRowStatus'
_N='juniRadiusAuthProxyCfgPortNumber'
_M='juniRadiusProxyUdpChecksum'
_L='juniRadiusAcctProxyCfgClientMask'
_K='juniRadiusAcctProxyCfgClientAddress'
_J='juniRadiusAuthProxyCfgClientMask'
_I='juniRadiusAuthProxyCfgClientAddress'
_H='TruthValue'
_G='read-write'
_F='DisplayString'
_E='Integer32'
_D='read-create'
_C='not-accessible'
_B='Juniper-RADIUS-Proxy-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
juniMibs,=mibBuilder.importSymbols('Juniper-MIBs','juniMibs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','RowStatus','TextualConvention',_H)
juniRadiusProxyMIB=ModuleIdentity((1,3,6,1,4,1,4874,2,2,73))
if mibBuilder.loadTexts:juniRadiusProxyMIB.setRevisions(('2004-01-23 19:32',))
_JuniRadiusProxyObjects_ObjectIdentity=ObjectIdentity
juniRadiusProxyObjects=_JuniRadiusProxyObjects_ObjectIdentity((1,3,6,1,4,1,4874,2,2,73,1))
_JuniRadiusGeneralProxy_ObjectIdentity=ObjectIdentity
juniRadiusGeneralProxy=_JuniRadiusGeneralProxy_ObjectIdentity((1,3,6,1,4,1,4874,2,2,73,1,1))
class _JuniRadiusProxyUdpChecksum_Type(TruthValue):defaultValue=1
_JuniRadiusProxyUdpChecksum_Type.__name__=_H
_JuniRadiusProxyUdpChecksum_Object=MibScalar
juniRadiusProxyUdpChecksum=_JuniRadiusProxyUdpChecksum_Object((1,3,6,1,4,1,4874,2,2,73,1,1,1),_JuniRadiusProxyUdpChecksum_Type())
juniRadiusProxyUdpChecksum.setMaxAccess(_G)
if mibBuilder.loadTexts:juniRadiusProxyUdpChecksum.setStatus(_A)
_JuniRadiusAuthProxyCfg_ObjectIdentity=ObjectIdentity
juniRadiusAuthProxyCfg=_JuniRadiusAuthProxyCfg_ObjectIdentity((1,3,6,1,4,1,4874,2,2,73,1,2))
class _JuniRadiusAuthProxyCfgPortNumber_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_JuniRadiusAuthProxyCfgPortNumber_Type.__name__=_E
_JuniRadiusAuthProxyCfgPortNumber_Object=MibScalar
juniRadiusAuthProxyCfgPortNumber=_JuniRadiusAuthProxyCfgPortNumber_Object((1,3,6,1,4,1,4874,2,2,73,1,2,1),_JuniRadiusAuthProxyCfgPortNumber_Type())
juniRadiusAuthProxyCfgPortNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:juniRadiusAuthProxyCfgPortNumber.setStatus(_A)
_JuniRadiusAuthProxyCfgClientTable_Object=MibTable
juniRadiusAuthProxyCfgClientTable=_JuniRadiusAuthProxyCfgClientTable_Object((1,3,6,1,4,1,4874,2,2,73,1,2,2))
if mibBuilder.loadTexts:juniRadiusAuthProxyCfgClientTable.setStatus(_A)
_JuniRadiusAuthProxyCfgClientEntry_Object=MibTableRow
juniRadiusAuthProxyCfgClientEntry=_JuniRadiusAuthProxyCfgClientEntry_Object((1,3,6,1,4,1,4874,2,2,73,1,2,2,1))
juniRadiusAuthProxyCfgClientEntry.setIndexNames((0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:juniRadiusAuthProxyCfgClientEntry.setStatus(_A)
_JuniRadiusAuthProxyCfgClientAddress_Type=IpAddress
_JuniRadiusAuthProxyCfgClientAddress_Object=MibTableColumn
juniRadiusAuthProxyCfgClientAddress=_JuniRadiusAuthProxyCfgClientAddress_Object((1,3,6,1,4,1,4874,2,2,73,1,2,2,1,1),_JuniRadiusAuthProxyCfgClientAddress_Type())
juniRadiusAuthProxyCfgClientAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:juniRadiusAuthProxyCfgClientAddress.setStatus(_A)
_JuniRadiusAuthProxyCfgClientMask_Type=IpAddress
_JuniRadiusAuthProxyCfgClientMask_Object=MibTableColumn
juniRadiusAuthProxyCfgClientMask=_JuniRadiusAuthProxyCfgClientMask_Object((1,3,6,1,4,1,4874,2,2,73,1,2,2,1,2),_JuniRadiusAuthProxyCfgClientMask_Type())
juniRadiusAuthProxyCfgClientMask.setMaxAccess(_C)
if mibBuilder.loadTexts:juniRadiusAuthProxyCfgClientMask.setStatus(_A)
_JuniRadiusAuthProxyCfgRowStatus_Type=RowStatus
_JuniRadiusAuthProxyCfgRowStatus_Object=MibTableColumn
juniRadiusAuthProxyCfgRowStatus=_JuniRadiusAuthProxyCfgRowStatus_Object((1,3,6,1,4,1,4874,2,2,73,1,2,2,1,3),_JuniRadiusAuthProxyCfgRowStatus_Type())
juniRadiusAuthProxyCfgRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:juniRadiusAuthProxyCfgRowStatus.setStatus(_A)
class _JuniRadiusAuthProxyCfgClientKey_Type(DisplayString):defaultHexValue='';subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_JuniRadiusAuthProxyCfgClientKey_Type.__name__=_F
_JuniRadiusAuthProxyCfgClientKey_Object=MibTableColumn
juniRadiusAuthProxyCfgClientKey=_JuniRadiusAuthProxyCfgClientKey_Object((1,3,6,1,4,1,4874,2,2,73,1,2,2,1,4),_JuniRadiusAuthProxyCfgClientKey_Type())
juniRadiusAuthProxyCfgClientKey.setMaxAccess(_D)
if mibBuilder.loadTexts:juniRadiusAuthProxyCfgClientKey.setStatus(_A)
_JuniRadiusAcctProxyCfg_ObjectIdentity=ObjectIdentity
juniRadiusAcctProxyCfg=_JuniRadiusAcctProxyCfg_ObjectIdentity((1,3,6,1,4,1,4874,2,2,73,1,3))
class _JuniRadiusAcctProxyCfgPortNumber_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_JuniRadiusAcctProxyCfgPortNumber_Type.__name__=_E
_JuniRadiusAcctProxyCfgPortNumber_Object=MibScalar
juniRadiusAcctProxyCfgPortNumber=_JuniRadiusAcctProxyCfgPortNumber_Object((1,3,6,1,4,1,4874,2,2,73,1,3,1),_JuniRadiusAcctProxyCfgPortNumber_Type())
juniRadiusAcctProxyCfgPortNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:juniRadiusAcctProxyCfgPortNumber.setStatus(_A)
_JuniRadiusAcctProxyCfgClientTable_Object=MibTable
juniRadiusAcctProxyCfgClientTable=_JuniRadiusAcctProxyCfgClientTable_Object((1,3,6,1,4,1,4874,2,2,73,1,3,2))
if mibBuilder.loadTexts:juniRadiusAcctProxyCfgClientTable.setStatus(_A)
_JuniRadiusAcctProxyCfgClientEntry_Object=MibTableRow
juniRadiusAcctProxyCfgClientEntry=_JuniRadiusAcctProxyCfgClientEntry_Object((1,3,6,1,4,1,4874,2,2,73,1,3,2,1))
juniRadiusAcctProxyCfgClientEntry.setIndexNames((0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:juniRadiusAcctProxyCfgClientEntry.setStatus(_A)
_JuniRadiusAcctProxyCfgClientAddress_Type=IpAddress
_JuniRadiusAcctProxyCfgClientAddress_Object=MibTableColumn
juniRadiusAcctProxyCfgClientAddress=_JuniRadiusAcctProxyCfgClientAddress_Object((1,3,6,1,4,1,4874,2,2,73,1,3,2,1,1),_JuniRadiusAcctProxyCfgClientAddress_Type())
juniRadiusAcctProxyCfgClientAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:juniRadiusAcctProxyCfgClientAddress.setStatus(_A)
_JuniRadiusAcctProxyCfgClientMask_Type=IpAddress
_JuniRadiusAcctProxyCfgClientMask_Object=MibTableColumn
juniRadiusAcctProxyCfgClientMask=_JuniRadiusAcctProxyCfgClientMask_Object((1,3,6,1,4,1,4874,2,2,73,1,3,2,1,2),_JuniRadiusAcctProxyCfgClientMask_Type())
juniRadiusAcctProxyCfgClientMask.setMaxAccess(_C)
if mibBuilder.loadTexts:juniRadiusAcctProxyCfgClientMask.setStatus(_A)
_JuniRadiusAcctProxyCfgRowStatus_Type=RowStatus
_JuniRadiusAcctProxyCfgRowStatus_Object=MibTableColumn
juniRadiusAcctProxyCfgRowStatus=_JuniRadiusAcctProxyCfgRowStatus_Object((1,3,6,1,4,1,4874,2,2,73,1,3,2,1,3),_JuniRadiusAcctProxyCfgRowStatus_Type())
juniRadiusAcctProxyCfgRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:juniRadiusAcctProxyCfgRowStatus.setStatus(_A)
class _JuniRadiusAcctProxyCfgClientKey_Type(DisplayString):defaultHexValue='';subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_JuniRadiusAcctProxyCfgClientKey_Type.__name__=_F
_JuniRadiusAcctProxyCfgClientKey_Object=MibTableColumn
juniRadiusAcctProxyCfgClientKey=_JuniRadiusAcctProxyCfgClientKey_Object((1,3,6,1,4,1,4874,2,2,73,1,3,2,1,4),_JuniRadiusAcctProxyCfgClientKey_Type())
juniRadiusAcctProxyCfgClientKey.setMaxAccess(_D)
if mibBuilder.loadTexts:juniRadiusAcctProxyCfgClientKey.setStatus(_A)
_JuniRadiusProxyMIBConformance_ObjectIdentity=ObjectIdentity
juniRadiusProxyMIBConformance=_JuniRadiusProxyMIBConformance_ObjectIdentity((1,3,6,1,4,1,4874,2,2,73,2))
_JuniRadiusProxyMIBCompliances_ObjectIdentity=ObjectIdentity
juniRadiusProxyMIBCompliances=_JuniRadiusProxyMIBCompliances_ObjectIdentity((1,3,6,1,4,1,4874,2,2,73,2,1))
_JuniRadiusProxyMIBGroups_ObjectIdentity=ObjectIdentity
juniRadiusProxyMIBGroups=_JuniRadiusProxyMIBGroups_ObjectIdentity((1,3,6,1,4,1,4874,2,2,73,2,2))
juniRadiusBasicProxyGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,73,2,2,1))
juniRadiusBasicProxyGroup.setObjects((_B,_M))
if mibBuilder.loadTexts:juniRadiusBasicProxyGroup.setStatus(_A)
juniRadiusAuthProxyGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,73,2,2,2))
juniRadiusAuthProxyGroup.setObjects(*((_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:juniRadiusAuthProxyGroup.setStatus(_A)
juniRadiusAcctProxyGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,73,2,2,3))
juniRadiusAcctProxyGroup.setObjects(*((_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:juniRadiusAcctProxyGroup.setStatus(_A)
juniRadiusProxyCompliance=ModuleCompliance((1,3,6,1,4,1,4874,2,2,73,2,1,1))
juniRadiusProxyCompliance.setObjects(*((_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:juniRadiusProxyCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'juniRadiusProxyMIB':juniRadiusProxyMIB,'juniRadiusProxyObjects':juniRadiusProxyObjects,'juniRadiusGeneralProxy':juniRadiusGeneralProxy,_M:juniRadiusProxyUdpChecksum,'juniRadiusAuthProxyCfg':juniRadiusAuthProxyCfg,_N:juniRadiusAuthProxyCfgPortNumber,'juniRadiusAuthProxyCfgClientTable':juniRadiusAuthProxyCfgClientTable,'juniRadiusAuthProxyCfgClientEntry':juniRadiusAuthProxyCfgClientEntry,_I:juniRadiusAuthProxyCfgClientAddress,_J:juniRadiusAuthProxyCfgClientMask,_O:juniRadiusAuthProxyCfgRowStatus,_P:juniRadiusAuthProxyCfgClientKey,'juniRadiusAcctProxyCfg':juniRadiusAcctProxyCfg,_Q:juniRadiusAcctProxyCfgPortNumber,'juniRadiusAcctProxyCfgClientTable':juniRadiusAcctProxyCfgClientTable,'juniRadiusAcctProxyCfgClientEntry':juniRadiusAcctProxyCfgClientEntry,_K:juniRadiusAcctProxyCfgClientAddress,_L:juniRadiusAcctProxyCfgClientMask,_R:juniRadiusAcctProxyCfgRowStatus,_S:juniRadiusAcctProxyCfgClientKey,'juniRadiusProxyMIBConformance':juniRadiusProxyMIBConformance,'juniRadiusProxyMIBCompliances':juniRadiusProxyMIBCompliances,'juniRadiusProxyCompliance':juniRadiusProxyCompliance,'juniRadiusProxyMIBGroups':juniRadiusProxyMIBGroups,_T:juniRadiusBasicProxyGroup,_U:juniRadiusAuthProxyGroup,_V:juniRadiusAcctProxyGroup})