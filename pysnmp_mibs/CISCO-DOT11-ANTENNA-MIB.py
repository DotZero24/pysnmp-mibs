_I='cDot11AntennaGlobalGroup'
_H='cDot11AntennaResultantGain'
_G='cDot11AntennaIsGainConfigured'
_F='read-only'
_E='Integer32'
_D='ifIndex'
_C='IF-MIB'
_B='CISCO-DOT11-ANTENNA-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_C,_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
ciscoDot11AntennaMIB=ModuleIdentity((1,3,6,1,4,1,9,9,384))
if mibBuilder.loadTexts:ciscoDot11AntennaMIB.setRevisions(('2016-02-15 00:00','2003-12-08 00:00'))
_CDot11AntennaMIBObjects_ObjectIdentity=ObjectIdentity
cDot11AntennaMIBObjects=_CDot11AntennaMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,384,1))
_CDot11AntennaGlobal_ObjectIdentity=ObjectIdentity
cDot11AntennaGlobal=_CDot11AntennaGlobal_ObjectIdentity((1,3,6,1,4,1,9,9,384,1,1))
_CDot11AntennaTable_Object=MibTable
cDot11AntennaTable=_CDot11AntennaTable_Object((1,3,6,1,4,1,9,9,384,1,1,1))
if mibBuilder.loadTexts:cDot11AntennaTable.setStatus(_A)
_CDot11AntennaEntry_Object=MibTableRow
cDot11AntennaEntry=_CDot11AntennaEntry_Object((1,3,6,1,4,1,9,9,384,1,1,1,1))
cDot11AntennaEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:cDot11AntennaEntry.setStatus(_A)
_CDot11AntennaIsGainConfigured_Type=TruthValue
_CDot11AntennaIsGainConfigured_Object=MibTableColumn
cDot11AntennaIsGainConfigured=_CDot11AntennaIsGainConfigured_Object((1,3,6,1,4,1,9,9,384,1,1,1,1,1),_CDot11AntennaIsGainConfigured_Type())
cDot11AntennaIsGainConfigured.setMaxAccess(_F)
if mibBuilder.loadTexts:cDot11AntennaIsGainConfigured.setStatus(_A)
class _CDot11AntennaResultantGain_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-128,128))
_CDot11AntennaResultantGain_Type.__name__=_E
_CDot11AntennaResultantGain_Object=MibTableColumn
cDot11AntennaResultantGain=_CDot11AntennaResultantGain_Object((1,3,6,1,4,1,9,9,384,1,1,1,1,2),_CDot11AntennaResultantGain_Type())
cDot11AntennaResultantGain.setMaxAccess(_F)
if mibBuilder.loadTexts:cDot11AntennaResultantGain.setStatus(_A)
_CDot11AntennaMIBConform_ObjectIdentity=ObjectIdentity
cDot11AntennaMIBConform=_CDot11AntennaMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,384,2))
_CDot11AntennaMIBCompliances_ObjectIdentity=ObjectIdentity
cDot11AntennaMIBCompliances=_CDot11AntennaMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,384,2,1))
_CDot11AntennaMIBGroups_ObjectIdentity=ObjectIdentity
cDot11AntennaMIBGroups=_CDot11AntennaMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,384,2,2))
cDot11AntennaGlobalGroup=ObjectGroup((1,3,6,1,4,1,9,9,384,2,2,1))
cDot11AntennaGlobalGroup.setObjects(*((_B,_G),(_B,_H)))
if mibBuilder.loadTexts:cDot11AntennaGlobalGroup.setStatus(_A)
cDot11AntennaMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,384,2,1,1))
cDot11AntennaMIBCompliance.setObjects((_B,_I))
if mibBuilder.loadTexts:cDot11AntennaMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoDot11AntennaMIB':ciscoDot11AntennaMIB,'cDot11AntennaMIBObjects':cDot11AntennaMIBObjects,'cDot11AntennaGlobal':cDot11AntennaGlobal,'cDot11AntennaTable':cDot11AntennaTable,'cDot11AntennaEntry':cDot11AntennaEntry,_G:cDot11AntennaIsGainConfigured,_H:cDot11AntennaResultantGain,'cDot11AntennaMIBConform':cDot11AntennaMIBConform,'cDot11AntennaMIBCompliances':cDot11AntennaMIBCompliances,'cDot11AntennaMIBCompliance':cDot11AntennaMIBCompliance,'cDot11AntennaMIBGroups':cDot11AntennaMIBGroups,_I:cDot11AntennaGlobalGroup})