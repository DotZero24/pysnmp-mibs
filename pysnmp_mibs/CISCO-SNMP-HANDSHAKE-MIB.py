_H='ciscoSnmpHandshakeGroup'
_G='csHandshakeCheck'
_F='csHandshakeUpdate'
_E='csHandshakeInit'
_D='read-only'
_C='OctetString'
_B='CISCO-SNMP-HANDSHAKE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
bsnWireless,=mibBuilder.importSymbols('AIRESPACE-WIRELESS-MIB','bsnWireless')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
ciscoSnmpHandshakeMIB=ModuleIdentity((1,3,6,1,4,1,14179,2,40))
if mibBuilder.loadTexts:ciscoSnmpHandshakeMIB.setRevisions(('2007-05-23 00:00',))
_CiscoSnmpHandshakeMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoSnmpHandshakeMIBNotifs=_CiscoSnmpHandshakeMIBNotifs_ObjectIdentity((1,3,6,1,4,1,14179,2,40,0))
_CiscoSnmpHandshakeMIBObjects_ObjectIdentity=ObjectIdentity
ciscoSnmpHandshakeMIBObjects=_CiscoSnmpHandshakeMIBObjects_ObjectIdentity((1,3,6,1,4,1,14179,2,40,1))
_CiscoSnmpHandshakeProcess_ObjectIdentity=ObjectIdentity
ciscoSnmpHandshakeProcess=_CiscoSnmpHandshakeProcess_ObjectIdentity((1,3,6,1,4,1,14179,2,40,1,1))
class _CsHandshakeInit_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_CsHandshakeInit_Type.__name__=_C
_CsHandshakeInit_Object=MibScalar
csHandshakeInit=_CsHandshakeInit_Object((1,3,6,1,4,1,14179,2,40,1,1,1),_CsHandshakeInit_Type())
csHandshakeInit.setMaxAccess(_D)
if mibBuilder.loadTexts:csHandshakeInit.setStatus(_A)
class _CsHandshakeUpdate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_CsHandshakeUpdate_Type.__name__=_C
_CsHandshakeUpdate_Object=MibScalar
csHandshakeUpdate=_CsHandshakeUpdate_Object((1,3,6,1,4,1,14179,2,40,1,1,2),_CsHandshakeUpdate_Type())
csHandshakeUpdate.setMaxAccess('read-write')
if mibBuilder.loadTexts:csHandshakeUpdate.setStatus(_A)
_CiscoSnmpHandshakeTest_ObjectIdentity=ObjectIdentity
ciscoSnmpHandshakeTest=_CiscoSnmpHandshakeTest_ObjectIdentity((1,3,6,1,4,1,14179,2,40,1,2))
_CsHandshakeCheck_Type=TruthValue
_CsHandshakeCheck_Object=MibScalar
csHandshakeCheck=_CsHandshakeCheck_Object((1,3,6,1,4,1,14179,2,40,1,2,1),_CsHandshakeCheck_Type())
csHandshakeCheck.setMaxAccess(_D)
if mibBuilder.loadTexts:csHandshakeCheck.setStatus(_A)
_CiscoSnmpHandshakeMIBConform_ObjectIdentity=ObjectIdentity
ciscoSnmpHandshakeMIBConform=_CiscoSnmpHandshakeMIBConform_ObjectIdentity((1,3,6,1,4,1,14179,2,40,2))
_CiscoSnmpHandshakeMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoSnmpHandshakeMIBCompliances=_CiscoSnmpHandshakeMIBCompliances_ObjectIdentity((1,3,6,1,4,1,14179,2,40,2,1))
_CiscoSnmpHandshakeMIBGroups_ObjectIdentity=ObjectIdentity
ciscoSnmpHandshakeMIBGroups=_CiscoSnmpHandshakeMIBGroups_ObjectIdentity((1,3,6,1,4,1,14179,2,40,2,2))
ciscoSnmpHandshakeGroup=ObjectGroup((1,3,6,1,4,1,14179,2,40,2,2,1))
ciscoSnmpHandshakeGroup.setObjects(*((_B,_E),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:ciscoSnmpHandshakeGroup.setStatus(_A)
ciscoSnmpHandshakeMIBCompliance=ModuleCompliance((1,3,6,1,4,1,14179,2,40,2,1,1))
ciscoSnmpHandshakeMIBCompliance.setObjects((_B,_H))
if mibBuilder.loadTexts:ciscoSnmpHandshakeMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoSnmpHandshakeMIB':ciscoSnmpHandshakeMIB,'ciscoSnmpHandshakeMIBNotifs':ciscoSnmpHandshakeMIBNotifs,'ciscoSnmpHandshakeMIBObjects':ciscoSnmpHandshakeMIBObjects,'ciscoSnmpHandshakeProcess':ciscoSnmpHandshakeProcess,_E:csHandshakeInit,_F:csHandshakeUpdate,'ciscoSnmpHandshakeTest':ciscoSnmpHandshakeTest,_G:csHandshakeCheck,'ciscoSnmpHandshakeMIBConform':ciscoSnmpHandshakeMIBConform,'ciscoSnmpHandshakeMIBCompliances':ciscoSnmpHandshakeMIBCompliances,'ciscoSnmpHandshakeMIBCompliance':ciscoSnmpHandshakeMIBCompliance,'ciscoSnmpHandshakeMIBGroups':ciscoSnmpHandshakeMIBGroups,_H:ciscoSnmpHandshakeGroup})