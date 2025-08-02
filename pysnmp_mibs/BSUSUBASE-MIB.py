_G='aniBsuWirelessPort'
_F='BSUWIRELESSIF-MIB'
_E='aniBsuSuMacAddr'
_D='BSUSUINV-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
aniBsuSuGroup,=mibBuilder.importSymbols('ANIROOT-MIB','aniBsuSuGroup')
aniBsuSuMacAddr,=mibBuilder.importSymbols(_D,_E)
aniBsuWirelessPort,=mibBuilder.importSymbols(_F,_G)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
aniBsuSuBase=ModuleIdentity((1,3,6,1,4,1,4325,3,7,2))
_AniBsuSuBaseTable_Object=MibTable
aniBsuSuBaseTable=_AniBsuSuBaseTable_Object((1,3,6,1,4,1,4325,3,7,2,1))
if mibBuilder.loadTexts:aniBsuSuBaseTable.setStatus(_A)
_AniBsuSuBaseEntry_Object=MibTableRow
aniBsuSuBaseEntry=_AniBsuSuBaseEntry_Object((1,3,6,1,4,1,4325,3,7,2,1,1))
aniBsuSuBaseEntry.setIndexNames((0,_F,_G),(0,_D,_E))
if mibBuilder.loadTexts:aniBsuSuBaseEntry.setStatus(_A)
class _AniBsuSuNetworkAccess_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_AniBsuSuNetworkAccess_Type.__name__=_C
_AniBsuSuNetworkAccess_Object=MibTableColumn
aniBsuSuNetworkAccess=_AniBsuSuNetworkAccess_Object((1,3,6,1,4,1,4325,3,7,2,1,1,2),_AniBsuSuNetworkAccess_Type())
aniBsuSuNetworkAccess.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuSuNetworkAccess.setStatus(_A)
class _AniBsuSuMaxHostSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_AniBsuSuMaxHostSupport_Type.__name__=_C
_AniBsuSuMaxHostSupport_Object=MibTableColumn
aniBsuSuMaxHostSupport=_AniBsuSuMaxHostSupport_Object((1,3,6,1,4,1,4325,3,7,2,1,1,3),_AniBsuSuMaxHostSupport_Type())
aniBsuSuMaxHostSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuSuMaxHostSupport.setStatus(_A)
_AniBsuSuTargetFreq_Type=DisplayString
_AniBsuSuTargetFreq_Object=MibTableColumn
aniBsuSuTargetFreq=_AniBsuSuTargetFreq_Object((1,3,6,1,4,1,4325,3,7,2,1,1,4),_AniBsuSuTargetFreq_Type())
aniBsuSuTargetFreq.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuSuTargetFreq.setStatus(_A)
_AniBsuSuFrequencyTable_Type=DisplayString
_AniBsuSuFrequencyTable_Object=MibTableColumn
aniBsuSuFrequencyTable=_AniBsuSuFrequencyTable_Object((1,3,6,1,4,1,4325,3,7,2,1,1,5),_AniBsuSuFrequencyTable_Type())
aniBsuSuFrequencyTable.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuSuFrequencyTable.setStatus(_A)
mibBuilder.exportSymbols('BSUSUBASE-MIB',**{'aniBsuSuBase':aniBsuSuBase,'aniBsuSuBaseTable':aniBsuSuBaseTable,'aniBsuSuBaseEntry':aniBsuSuBaseEntry,'aniBsuSuNetworkAccess':aniBsuSuNetworkAccess,'aniBsuSuMaxHostSupport':aniBsuSuMaxHostSupport,'aniBsuSuTargetFreq':aniBsuSuTargetFreq,'aniBsuSuFrequencyTable':aniBsuSuFrequencyTable})