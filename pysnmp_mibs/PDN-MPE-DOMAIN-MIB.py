_H='mpePdnCardConfigVnidId'
_G='PDN-MPE-DOMAIN-MIB'
_F='read-only'
_E='NotificationType'
_D='entPhysicalIndex'
_C='ENTITY-MIB'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols(_C,_D)
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
mpe_domain,=mibBuilder.importSymbols('PDN-HEADER-MIB','mpe-domain')
ClientState,SwitchState,VnidRange,VnidTaggingState=mibBuilder.importSymbols('PDN-TC','ClientState','SwitchState','VnidRange','VnidTaggingState')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier',_E,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_E,'TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
_MpePdnDomainMIBObjects_ObjectIdentity=ObjectIdentity
mpePdnDomainMIBObjects=_MpePdnDomainMIBObjects_ObjectIdentity((1,3,6,1,4,1,1795,2,24,12,22,1))
_MpePdnCardGeneralParams_ObjectIdentity=ObjectIdentity
mpePdnCardGeneralParams=_MpePdnCardGeneralParams_ObjectIdentity((1,3,6,1,4,1,1795,2,24,12,22,1,1))
_MpePdnCardGeneralParamsTable_Object=MibTable
mpePdnCardGeneralParamsTable=_MpePdnCardGeneralParamsTable_Object((1,3,6,1,4,1,1795,2,24,12,22,1,1,1))
if mibBuilder.loadTexts:mpePdnCardGeneralParamsTable.setStatus(_A)
_MpePdnCardGeneralParamsEntry_Object=MibTableRow
mpePdnCardGeneralParamsEntry=_MpePdnCardGeneralParamsEntry_Object((1,3,6,1,4,1,1795,2,24,12,22,1,1,1,1))
mpePdnCardGeneralParamsEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:mpePdnCardGeneralParamsEntry.setStatus(_A)
_MpePdnCardGeneralParamsVNIDMode_Type=VnidTaggingState
_MpePdnCardGeneralParamsVNIDMode_Object=MibTableColumn
mpePdnCardGeneralParamsVNIDMode=_MpePdnCardGeneralParamsVNIDMode_Object((1,3,6,1,4,1,1795,2,24,12,22,1,1,1,1,1),_MpePdnCardGeneralParamsVNIDMode_Type())
mpePdnCardGeneralParamsVNIDMode.setMaxAccess(_B)
if mibBuilder.loadTexts:mpePdnCardGeneralParamsVNIDMode.setStatus(_A)
_MpePdnCardGeneralParamsAdditionalClientsAvailable_Type=Integer32
_MpePdnCardGeneralParamsAdditionalClientsAvailable_Object=MibTableColumn
mpePdnCardGeneralParamsAdditionalClientsAvailable=_MpePdnCardGeneralParamsAdditionalClientsAvailable_Object((1,3,6,1,4,1,1795,2,24,12,22,1,1,1,1,2),_MpePdnCardGeneralParamsAdditionalClientsAvailable_Type())
mpePdnCardGeneralParamsAdditionalClientsAvailable.setMaxAccess(_F)
if mibBuilder.loadTexts:mpePdnCardGeneralParamsAdditionalClientsAvailable.setStatus(_A)
_MpePdnCardConfig_ObjectIdentity=ObjectIdentity
mpePdnCardConfig=_MpePdnCardConfig_ObjectIdentity((1,3,6,1,4,1,1795,2,24,12,22,1,2))
_MpePdnCardConfigTable_Object=MibTable
mpePdnCardConfigTable=_MpePdnCardConfigTable_Object((1,3,6,1,4,1,1795,2,24,12,22,1,2,1))
if mibBuilder.loadTexts:mpePdnCardConfigTable.setStatus(_A)
_MpePdnCardConfigEntry_Object=MibTableRow
mpePdnCardConfigEntry=_MpePdnCardConfigEntry_Object((1,3,6,1,4,1,1795,2,24,12,22,1,2,1,1))
mpePdnCardConfigEntry.setIndexNames((0,_C,_D),(0,_G,_H))
if mibBuilder.loadTexts:mpePdnCardConfigEntry.setStatus(_A)
_MpePdnCardConfigVnidId_Type=VnidRange
_MpePdnCardConfigVnidId_Object=MibTableColumn
mpePdnCardConfigVnidId=_MpePdnCardConfigVnidId_Object((1,3,6,1,4,1,1795,2,24,12,22,1,2,1,1,1),_MpePdnCardConfigVnidId_Type())
mpePdnCardConfigVnidId.setMaxAccess(_F)
if mibBuilder.loadTexts:mpePdnCardConfigVnidId.setStatus(_A)
_MpePdnCardConfigDomainName_Type=DisplayString
_MpePdnCardConfigDomainName_Object=MibTableColumn
mpePdnCardConfigDomainName=_MpePdnCardConfigDomainName_Object((1,3,6,1,4,1,1795,2,24,12,22,1,2,1,1,2),_MpePdnCardConfigDomainName_Type())
mpePdnCardConfigDomainName.setMaxAccess(_B)
if mibBuilder.loadTexts:mpePdnCardConfigDomainName.setStatus(_A)
_MpePdnCardConfigMuxFwd_Type=SwitchState
_MpePdnCardConfigMuxFwd_Object=MibTableColumn
mpePdnCardConfigMuxFwd=_MpePdnCardConfigMuxFwd_Object((1,3,6,1,4,1,1795,2,24,12,22,1,2,1,1,3),_MpePdnCardConfigMuxFwd_Type())
mpePdnCardConfigMuxFwd.setMaxAccess(_B)
if mibBuilder.loadTexts:mpePdnCardConfigMuxFwd.setStatus(_A)
_MpePdnCardConfigIPFiltering_Type=SwitchState
_MpePdnCardConfigIPFiltering_Object=MibTableColumn
mpePdnCardConfigIPFiltering=_MpePdnCardConfigIPFiltering_Object((1,3,6,1,4,1,1795,2,24,12,22,1,2,1,1,4),_MpePdnCardConfigIPFiltering_Type())
mpePdnCardConfigIPFiltering.setMaxAccess(_B)
if mibBuilder.loadTexts:mpePdnCardConfigIPFiltering.setStatus(_A)
_MpePdnCardConfigIPScoping_Type=SwitchState
_MpePdnCardConfigIPScoping_Object=MibTableColumn
mpePdnCardConfigIPScoping=_MpePdnCardConfigIPScoping_Object((1,3,6,1,4,1,1795,2,24,12,22,1,2,1,1,5),_MpePdnCardConfigIPScoping_Type())
mpePdnCardConfigIPScoping.setMaxAccess(_B)
if mibBuilder.loadTexts:mpePdnCardConfigIPScoping.setStatus(_A)
_MpePdnCardConfigVnidAuth_Type=SwitchState
_MpePdnCardConfigVnidAuth_Object=MibTableColumn
mpePdnCardConfigVnidAuth=_MpePdnCardConfigVnidAuth_Object((1,3,6,1,4,1,1795,2,24,12,22,1,2,1,1,6),_MpePdnCardConfigVnidAuth_Type())
mpePdnCardConfigVnidAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:mpePdnCardConfigVnidAuth.setStatus(_A)
_MpePdnCardConfigRowStatus_Type=RowStatus
_MpePdnCardConfigRowStatus_Object=MibTableColumn
mpePdnCardConfigRowStatus=_MpePdnCardConfigRowStatus_Object((1,3,6,1,4,1,1795,2,24,12,22,1,2,1,1,7),_MpePdnCardConfigRowStatus_Type())
mpePdnCardConfigRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mpePdnCardConfigRowStatus.setStatus(_A)
_MpePdnDomainMIBTraps_ObjectIdentity=ObjectIdentity
mpePdnDomainMIBTraps=_MpePdnDomainMIBTraps_ObjectIdentity((1,3,6,1,4,1,1795,2,24,12,22,2))
mibBuilder.exportSymbols(_G,**{'mpePdnDomainMIBObjects':mpePdnDomainMIBObjects,'mpePdnCardGeneralParams':mpePdnCardGeneralParams,'mpePdnCardGeneralParamsTable':mpePdnCardGeneralParamsTable,'mpePdnCardGeneralParamsEntry':mpePdnCardGeneralParamsEntry,'mpePdnCardGeneralParamsVNIDMode':mpePdnCardGeneralParamsVNIDMode,'mpePdnCardGeneralParamsAdditionalClientsAvailable':mpePdnCardGeneralParamsAdditionalClientsAvailable,'mpePdnCardConfig':mpePdnCardConfig,'mpePdnCardConfigTable':mpePdnCardConfigTable,'mpePdnCardConfigEntry':mpePdnCardConfigEntry,_H:mpePdnCardConfigVnidId,'mpePdnCardConfigDomainName':mpePdnCardConfigDomainName,'mpePdnCardConfigMuxFwd':mpePdnCardConfigMuxFwd,'mpePdnCardConfigIPFiltering':mpePdnCardConfigIPFiltering,'mpePdnCardConfigIPScoping':mpePdnCardConfigIPScoping,'mpePdnCardConfigVnidAuth':mpePdnCardConfigVnidAuth,'mpePdnCardConfigRowStatus':mpePdnCardConfigRowStatus,'mpePdnDomainMIBTraps':mpePdnDomainMIBTraps})