_K='ctMMACFENBCfgPort'
_J='ctMMACFENBCfgPortGroup'
_I='ctMMACFENBCfgInterface'
_H='ctFastEthernetCtlPort'
_G='ctFastEthernetCtlPortGroup'
_F='ctFastEthernetCtlInterface'
_E='read-write'
_D='FAST-ETHERNET-MIB'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ctFastEthernet,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctFastEthernet')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_CtFastEthernetCtl_ObjectIdentity=ObjectIdentity
ctFastEthernetCtl=_CtFastEthernetCtl_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,9,1))
_CtFastEthernetCtlTable_Object=MibTable
ctFastEthernetCtlTable=_CtFastEthernetCtlTable_Object((1,3,6,1,4,1,52,4,1,2,9,1,1))
if mibBuilder.loadTexts:ctFastEthernetCtlTable.setStatus(_A)
_CtFastEthernetCtlEntry_Object=MibTableRow
ctFastEthernetCtlEntry=_CtFastEthernetCtlEntry_Object((1,3,6,1,4,1,52,4,1,2,9,1,1,1))
ctFastEthernetCtlEntry.setIndexNames((0,_D,_F),(0,_D,_G),(0,_D,_H))
if mibBuilder.loadTexts:ctFastEthernetCtlEntry.setStatus(_A)
_CtFastEthernetCtlInterface_Type=Integer32
_CtFastEthernetCtlInterface_Object=MibTableColumn
ctFastEthernetCtlInterface=_CtFastEthernetCtlInterface_Object((1,3,6,1,4,1,52,4,1,2,9,1,1,1,1),_CtFastEthernetCtlInterface_Type())
ctFastEthernetCtlInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFastEthernetCtlInterface.setStatus(_A)
_CtFastEthernetCtlPortGroup_Type=Integer32
_CtFastEthernetCtlPortGroup_Object=MibTableColumn
ctFastEthernetCtlPortGroup=_CtFastEthernetCtlPortGroup_Object((1,3,6,1,4,1,52,4,1,2,9,1,1,1,2),_CtFastEthernetCtlPortGroup_Type())
ctFastEthernetCtlPortGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFastEthernetCtlPortGroup.setStatus(_A)
_CtFastEthernetCtlPort_Type=Integer32
_CtFastEthernetCtlPort_Object=MibTableColumn
ctFastEthernetCtlPort=_CtFastEthernetCtlPort_Object((1,3,6,1,4,1,52,4,1,2,9,1,1,1,3),_CtFastEthernetCtlPort_Type())
ctFastEthernetCtlPort.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFastEthernetCtlPort.setStatus(_A)
class _CtFastEthernetLocalTechnologyAbility_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1023))
_CtFastEthernetLocalTechnologyAbility_Type.__name__=_C
_CtFastEthernetLocalTechnologyAbility_Object=MibTableColumn
ctFastEthernetLocalTechnologyAbility=_CtFastEthernetLocalTechnologyAbility_Object((1,3,6,1,4,1,52,4,1,2,9,1,1,1,4),_CtFastEthernetLocalTechnologyAbility_Type())
ctFastEthernetLocalTechnologyAbility.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFastEthernetLocalTechnologyAbility.setStatus(_A)
class _CtFastEthernetCurrentOperationalMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1023))
_CtFastEthernetCurrentOperationalMode_Type.__name__=_C
_CtFastEthernetCurrentOperationalMode_Object=MibTableColumn
ctFastEthernetCurrentOperationalMode=_CtFastEthernetCurrentOperationalMode_Object((1,3,6,1,4,1,52,4,1,2,9,1,1,1,5),_CtFastEthernetCurrentOperationalMode_Type())
ctFastEthernetCurrentOperationalMode.setMaxAccess(_E)
if mibBuilder.loadTexts:ctFastEthernetCurrentOperationalMode.setStatus(_A)
class _CtFastEthernetAdvertisedTechnologyAbility_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1023))
_CtFastEthernetAdvertisedTechnologyAbility_Type.__name__=_C
_CtFastEthernetAdvertisedTechnologyAbility_Object=MibTableColumn
ctFastEthernetAdvertisedTechnologyAbility=_CtFastEthernetAdvertisedTechnologyAbility_Object((1,3,6,1,4,1,52,4,1,2,9,1,1,1,6),_CtFastEthernetAdvertisedTechnologyAbility_Type())
ctFastEthernetAdvertisedTechnologyAbility.setMaxAccess(_E)
if mibBuilder.loadTexts:ctFastEthernetAdvertisedTechnologyAbility.setStatus(_A)
class _CtFastEthernetReceivedTechnologyAbility_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1023))
_CtFastEthernetReceivedTechnologyAbility_Type.__name__=_C
_CtFastEthernetReceivedTechnologyAbility_Object=MibTableColumn
ctFastEthernetReceivedTechnologyAbility=_CtFastEthernetReceivedTechnologyAbility_Object((1,3,6,1,4,1,52,4,1,2,9,1,1,1,7),_CtFastEthernetReceivedTechnologyAbility_Type())
ctFastEthernetReceivedTechnologyAbility.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFastEthernetReceivedTechnologyAbility.setStatus(_A)
_CtFastEthernetCtlTableNumEntries_Type=Integer32
_CtFastEthernetCtlTableNumEntries_Object=MibScalar
ctFastEthernetCtlTableNumEntries=_CtFastEthernetCtlTableNumEntries_Object((1,3,6,1,4,1,52,4,1,2,9,1,2),_CtFastEthernetCtlTableNumEntries_Type())
ctFastEthernetCtlTableNumEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFastEthernetCtlTableNumEntries.setStatus(_A)
_CtMMACFENBCfg_ObjectIdentity=ObjectIdentity
ctMMACFENBCfg=_CtMMACFENBCfg_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,9,2))
_CtMMACFENBCfgTable_Object=MibTable
ctMMACFENBCfgTable=_CtMMACFENBCfgTable_Object((1,3,6,1,4,1,52,4,1,2,9,2,1))
if mibBuilder.loadTexts:ctMMACFENBCfgTable.setStatus(_A)
_CtMMACFENBCfgEntry_Object=MibTableRow
ctMMACFENBCfgEntry=_CtMMACFENBCfgEntry_Object((1,3,6,1,4,1,52,4,1,2,9,2,1,1))
ctMMACFENBCfgEntry.setIndexNames((0,_D,_I),(0,_D,_J),(0,_D,_K))
if mibBuilder.loadTexts:ctMMACFENBCfgEntry.setStatus(_A)
_CtMMACFENBCfgInterface_Type=Integer32
_CtMMACFENBCfgInterface_Object=MibTableColumn
ctMMACFENBCfgInterface=_CtMMACFENBCfgInterface_Object((1,3,6,1,4,1,52,4,1,2,9,2,1,1,1),_CtMMACFENBCfgInterface_Type())
ctMMACFENBCfgInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:ctMMACFENBCfgInterface.setStatus(_A)
_CtMMACFENBCfgPortGroup_Type=Integer32
_CtMMACFENBCfgPortGroup_Object=MibTableColumn
ctMMACFENBCfgPortGroup=_CtMMACFENBCfgPortGroup_Object((1,3,6,1,4,1,52,4,1,2,9,2,1,1,2),_CtMMACFENBCfgPortGroup_Type())
ctMMACFENBCfgPortGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:ctMMACFENBCfgPortGroup.setStatus(_A)
_CtMMACFENBCfgPort_Type=Integer32
_CtMMACFENBCfgPort_Object=MibTableColumn
ctMMACFENBCfgPort=_CtMMACFENBCfgPort_Object((1,3,6,1,4,1,52,4,1,2,9,2,1,1,3),_CtMMACFENBCfgPort_Type())
ctMMACFENBCfgPort.setMaxAccess(_B)
if mibBuilder.loadTexts:ctMMACFENBCfgPort.setStatus(_A)
class _CtMMACFENBOperCapabilities_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,63))
_CtMMACFENBOperCapabilities_Type.__name__=_C
_CtMMACFENBOperCapabilities_Object=MibTableColumn
ctMMACFENBOperCapabilities=_CtMMACFENBOperCapabilities_Object((1,3,6,1,4,1,52,4,1,2,9,2,1,1,4),_CtMMACFENBOperCapabilities_Type())
ctMMACFENBOperCapabilities.setMaxAccess(_B)
if mibBuilder.loadTexts:ctMMACFENBOperCapabilities.setStatus(_A)
class _CtMMACFENBAdminCapabilities_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,63))
_CtMMACFENBAdminCapabilities_Type.__name__=_C
_CtMMACFENBAdminCapabilities_Object=MibTableColumn
ctMMACFENBAdminCapabilities=_CtMMACFENBAdminCapabilities_Object((1,3,6,1,4,1,52,4,1,2,9,2,1,1,5),_CtMMACFENBAdminCapabilities_Type())
ctMMACFENBAdminCapabilities.setMaxAccess(_E)
if mibBuilder.loadTexts:ctMMACFENBAdminCapabilities.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'ctFastEthernetCtl':ctFastEthernetCtl,'ctFastEthernetCtlTable':ctFastEthernetCtlTable,'ctFastEthernetCtlEntry':ctFastEthernetCtlEntry,_F:ctFastEthernetCtlInterface,_G:ctFastEthernetCtlPortGroup,_H:ctFastEthernetCtlPort,'ctFastEthernetLocalTechnologyAbility':ctFastEthernetLocalTechnologyAbility,'ctFastEthernetCurrentOperationalMode':ctFastEthernetCurrentOperationalMode,'ctFastEthernetAdvertisedTechnologyAbility':ctFastEthernetAdvertisedTechnologyAbility,'ctFastEthernetReceivedTechnologyAbility':ctFastEthernetReceivedTechnologyAbility,'ctFastEthernetCtlTableNumEntries':ctFastEthernetCtlTableNumEntries,'ctMMACFENBCfg':ctMMACFENBCfg,'ctMMACFENBCfgTable':ctMMACFENBCfgTable,'ctMMACFENBCfgEntry':ctMMACFENBCfgEntry,_I:ctMMACFENBCfgInterface,_J:ctMMACFENBCfgPortGroup,_K:ctMMACFENBCfgPort,'ctMMACFENBOperCapabilities':ctMMACFENBOperCapabilities,'ctMMACFENBAdminCapabilities':ctMMACFENBAdminCapabilities})