_J='h3cL4RedirectVlanID'
_I='h3cL4RedirectIpExclusionIpAddress'
_H='h3cL4RedirectCacheIpAddress'
_G='DisplayString'
_F='not-accessible'
_E='Integer32'
_D='A3COM-HUAWEI-L4RDT-MIB'
_C='read-only'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','h3cCommon')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_G,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
h3cL4Redirect=ModuleIdentity((1,3,6,1,4,1,43,45,1,10,2,10))
_H3cL4RedirectCacheTable_Object=MibTable
h3cL4RedirectCacheTable=_H3cL4RedirectCacheTable_Object((1,3,6,1,4,1,43,45,1,10,2,10,1))
if mibBuilder.loadTexts:h3cL4RedirectCacheTable.setStatus(_A)
_H3cL4RedirectCacheEntry_Object=MibTableRow
h3cL4RedirectCacheEntry=_H3cL4RedirectCacheEntry_Object((1,3,6,1,4,1,43,45,1,10,2,10,1,1))
h3cL4RedirectCacheEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:h3cL4RedirectCacheEntry.setStatus(_A)
_H3cL4RedirectCacheIpAddress_Type=IpAddress
_H3cL4RedirectCacheIpAddress_Object=MibTableColumn
h3cL4RedirectCacheIpAddress=_H3cL4RedirectCacheIpAddress_Object((1,3,6,1,4,1,43,45,1,10,2,10,1,1,1),_H3cL4RedirectCacheIpAddress_Type())
h3cL4RedirectCacheIpAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cL4RedirectCacheIpAddress.setStatus(_A)
class _H3cL4RedirectCacheRedirectionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('disabledNotRedirecting',1),('enabledNoHealthChecker',2),('enabledHealthChecking',3),('enabledHealthCheckOKNotRedirecting',4),('enabledHealthCheckFailed',5),('enabledRedirecting',6)))
_H3cL4RedirectCacheRedirectionStatus_Type.__name__=_E
_H3cL4RedirectCacheRedirectionStatus_Object=MibTableColumn
h3cL4RedirectCacheRedirectionStatus=_H3cL4RedirectCacheRedirectionStatus_Object((1,3,6,1,4,1,43,45,1,10,2,10,1,1,2),_H3cL4RedirectCacheRedirectionStatus_Type())
h3cL4RedirectCacheRedirectionStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cL4RedirectCacheRedirectionStatus.setStatus(_A)
_H3cL4RedirectCachePort_Type=Integer32
_H3cL4RedirectCachePort_Object=MibTableColumn
h3cL4RedirectCachePort=_H3cL4RedirectCachePort_Object((1,3,6,1,4,1,43,45,1,10,2,10,1,1,3),_H3cL4RedirectCachePort_Type())
h3cL4RedirectCachePort.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cL4RedirectCachePort.setStatus(_A)
_H3cL4RedirectCacheRowStatus_Type=RowStatus
_H3cL4RedirectCacheRowStatus_Object=MibTableColumn
h3cL4RedirectCacheRowStatus=_H3cL4RedirectCacheRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,10,1,1,4),_H3cL4RedirectCacheRowStatus_Type())
h3cL4RedirectCacheRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cL4RedirectCacheRowStatus.setStatus(_A)
_H3cL4RedirectCacheMacAddress_Type=MacAddress
_H3cL4RedirectCacheMacAddress_Object=MibTableColumn
h3cL4RedirectCacheMacAddress=_H3cL4RedirectCacheMacAddress_Object((1,3,6,1,4,1,43,45,1,10,2,10,1,1,5),_H3cL4RedirectCacheMacAddress_Type())
h3cL4RedirectCacheMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cL4RedirectCacheMacAddress.setStatus(_A)
_H3cL4RedirectCacheVlan_Type=Integer32
_H3cL4RedirectCacheVlan_Object=MibTableColumn
h3cL4RedirectCacheVlan=_H3cL4RedirectCacheVlan_Object((1,3,6,1,4,1,43,45,1,10,2,10,1,1,6),_H3cL4RedirectCacheVlan_Type())
h3cL4RedirectCacheVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cL4RedirectCacheVlan.setStatus(_A)
_H3cL4RedirectCacheTcpPort_Type=Integer32
_H3cL4RedirectCacheTcpPort_Object=MibTableColumn
h3cL4RedirectCacheTcpPort=_H3cL4RedirectCacheTcpPort_Object((1,3,6,1,4,1,43,45,1,10,2,10,1,1,7),_H3cL4RedirectCacheTcpPort_Type())
h3cL4RedirectCacheTcpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cL4RedirectCacheTcpPort.setStatus(_A)
_H3cL4RedirectIpExclusionTable_Object=MibTable
h3cL4RedirectIpExclusionTable=_H3cL4RedirectIpExclusionTable_Object((1,3,6,1,4,1,43,45,1,10,2,10,2))
if mibBuilder.loadTexts:h3cL4RedirectIpExclusionTable.setStatus(_A)
_H3cL4RedirectIpExclusionEntry_Object=MibTableRow
h3cL4RedirectIpExclusionEntry=_H3cL4RedirectIpExclusionEntry_Object((1,3,6,1,4,1,43,45,1,10,2,10,2,1))
h3cL4RedirectIpExclusionEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:h3cL4RedirectIpExclusionEntry.setStatus(_A)
_H3cL4RedirectIpExclusionIpAddress_Type=IpAddress
_H3cL4RedirectIpExclusionIpAddress_Object=MibTableColumn
h3cL4RedirectIpExclusionIpAddress=_H3cL4RedirectIpExclusionIpAddress_Object((1,3,6,1,4,1,43,45,1,10,2,10,2,1,1),_H3cL4RedirectIpExclusionIpAddress_Type())
h3cL4RedirectIpExclusionIpAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cL4RedirectIpExclusionIpAddress.setStatus(_A)
class _H3cL4RedirectIpExclusionMaskLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_H3cL4RedirectIpExclusionMaskLen_Type.__name__=_E
_H3cL4RedirectIpExclusionMaskLen_Object=MibTableColumn
h3cL4RedirectIpExclusionMaskLen=_H3cL4RedirectIpExclusionMaskLen_Object((1,3,6,1,4,1,43,45,1,10,2,10,2,1,2),_H3cL4RedirectIpExclusionMaskLen_Type())
h3cL4RedirectIpExclusionMaskLen.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cL4RedirectIpExclusionMaskLen.setStatus(_A)
_H3cL4RedirectIpExclusionRowStatus_Type=RowStatus
_H3cL4RedirectIpExclusionRowStatus_Object=MibTableColumn
h3cL4RedirectIpExclusionRowStatus=_H3cL4RedirectIpExclusionRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,10,2,1,3),_H3cL4RedirectIpExclusionRowStatus_Type())
h3cL4RedirectIpExclusionRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cL4RedirectIpExclusionRowStatus.setStatus(_A)
_H3cL4RedirectVlanTable_Object=MibTable
h3cL4RedirectVlanTable=_H3cL4RedirectVlanTable_Object((1,3,6,1,4,1,43,45,1,10,2,10,3))
if mibBuilder.loadTexts:h3cL4RedirectVlanTable.setStatus(_A)
_H3cL4RedirectVlanEntry_Object=MibTableRow
h3cL4RedirectVlanEntry=_H3cL4RedirectVlanEntry_Object((1,3,6,1,4,1,43,45,1,10,2,10,3,1))
h3cL4RedirectVlanEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:h3cL4RedirectVlanEntry.setStatus(_A)
_H3cL4RedirectVlanID_Type=Integer32
_H3cL4RedirectVlanID_Object=MibTableColumn
h3cL4RedirectVlanID=_H3cL4RedirectVlanID_Object((1,3,6,1,4,1,43,45,1,10,2,10,3,1,1),_H3cL4RedirectVlanID_Type())
h3cL4RedirectVlanID.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cL4RedirectVlanID.setStatus(_A)
_H3cL4RedirectVlanRowStatus_Type=RowStatus
_H3cL4RedirectVlanRowStatus_Object=MibTableColumn
h3cL4RedirectVlanRowStatus=_H3cL4RedirectVlanRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,10,3,1,2),_H3cL4RedirectVlanRowStatus_Type())
h3cL4RedirectVlanRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cL4RedirectVlanRowStatus.setStatus(_A)
class _H3cL4RedirectInformationString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_H3cL4RedirectInformationString_Type.__name__=_G
_H3cL4RedirectInformationString_Object=MibScalar
h3cL4RedirectInformationString=_H3cL4RedirectInformationString_Object((1,3,6,1,4,1,43,45,1,10,2,10,4),_H3cL4RedirectInformationString_Type())
h3cL4RedirectInformationString.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cL4RedirectInformationString.setStatus(_A)
_H3cL4RedirectFreeCacheEntries_Type=Integer32
_H3cL4RedirectFreeCacheEntries_Object=MibScalar
h3cL4RedirectFreeCacheEntries=_H3cL4RedirectFreeCacheEntries_Object((1,3,6,1,4,1,43,45,1,10,2,10,5),_H3cL4RedirectFreeCacheEntries_Type())
h3cL4RedirectFreeCacheEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cL4RedirectFreeCacheEntries.setStatus(_A)
_H3cL4RedirectFreeIpExclusionEntries_Type=Integer32
_H3cL4RedirectFreeIpExclusionEntries_Object=MibScalar
h3cL4RedirectFreeIpExclusionEntries=_H3cL4RedirectFreeIpExclusionEntries_Object((1,3,6,1,4,1,43,45,1,10,2,10,6),_H3cL4RedirectFreeIpExclusionEntries_Type())
h3cL4RedirectFreeIpExclusionEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cL4RedirectFreeIpExclusionEntries.setStatus(_A)
_H3cL4RedirectFreeVlanEntries_Type=Integer32
_H3cL4RedirectFreeVlanEntries_Object=MibScalar
h3cL4RedirectFreeVlanEntries=_H3cL4RedirectFreeVlanEntries_Object((1,3,6,1,4,1,43,45,1,10,2,10,7),_H3cL4RedirectFreeVlanEntries_Type())
h3cL4RedirectFreeVlanEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cL4RedirectFreeVlanEntries.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'h3cL4Redirect':h3cL4Redirect,'h3cL4RedirectCacheTable':h3cL4RedirectCacheTable,'h3cL4RedirectCacheEntry':h3cL4RedirectCacheEntry,_H:h3cL4RedirectCacheIpAddress,'h3cL4RedirectCacheRedirectionStatus':h3cL4RedirectCacheRedirectionStatus,'h3cL4RedirectCachePort':h3cL4RedirectCachePort,'h3cL4RedirectCacheRowStatus':h3cL4RedirectCacheRowStatus,'h3cL4RedirectCacheMacAddress':h3cL4RedirectCacheMacAddress,'h3cL4RedirectCacheVlan':h3cL4RedirectCacheVlan,'h3cL4RedirectCacheTcpPort':h3cL4RedirectCacheTcpPort,'h3cL4RedirectIpExclusionTable':h3cL4RedirectIpExclusionTable,'h3cL4RedirectIpExclusionEntry':h3cL4RedirectIpExclusionEntry,_I:h3cL4RedirectIpExclusionIpAddress,'h3cL4RedirectIpExclusionMaskLen':h3cL4RedirectIpExclusionMaskLen,'h3cL4RedirectIpExclusionRowStatus':h3cL4RedirectIpExclusionRowStatus,'h3cL4RedirectVlanTable':h3cL4RedirectVlanTable,'h3cL4RedirectVlanEntry':h3cL4RedirectVlanEntry,_J:h3cL4RedirectVlanID,'h3cL4RedirectVlanRowStatus':h3cL4RedirectVlanRowStatus,'h3cL4RedirectInformationString':h3cL4RedirectInformationString,'h3cL4RedirectFreeCacheEntries':h3cL4RedirectFreeCacheEntries,'h3cL4RedirectFreeIpExclusionEntries':h3cL4RedirectFreeIpExclusionEntries,'h3cL4RedirectFreeVlanEntries':h3cL4RedirectFreeVlanEntries})