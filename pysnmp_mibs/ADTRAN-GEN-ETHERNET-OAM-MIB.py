if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adIdentityShared,adShared=mibBuilder.importSymbols('ADTRAN-MIB','adIdentityShared','adShared')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adGenEthernetOAMIdentity=ModuleIdentity((1,3,6,1,4,1,664,6,10000,75))
if mibBuilder.loadTexts:adGenEthernetOAMIdentity.setRevisions(('2011-06-10 08:00',))
_AdGenEthernetOAM_ObjectIdentity=ObjectIdentity
adGenEthernetOAM=_AdGenEthernetOAM_ObjectIdentity((1,3,6,1,4,1,664,5,75))
_AdGenEthernetCfm_ObjectIdentity=ObjectIdentity
adGenEthernetCfm=_AdGenEthernetCfm_ObjectIdentity((1,3,6,1,4,1,664,5,75,1))
_AdGenY1731_ObjectIdentity=ObjectIdentity
adGenY1731=_AdGenY1731_ObjectIdentity((1,3,6,1,4,1,664,5,75,2))
_AdGenEthernetCfmID_ObjectIdentity=ObjectIdentity
adGenEthernetCfmID=_AdGenEthernetCfmID_ObjectIdentity((1,3,6,1,4,1,664,6,10000,75,1))
_AdGenY1731ID_ObjectIdentity=ObjectIdentity
adGenY1731ID=_AdGenY1731ID_ObjectIdentity((1,3,6,1,4,1,664,6,10000,75,2))
mibBuilder.exportSymbols('ADTRAN-GEN-ETHERNET-OAM-MIB',**{'adGenEthernetOAM':adGenEthernetOAM,'adGenEthernetCfm':adGenEthernetCfm,'adGenY1731':adGenY1731,'adGenEthernetOAMIdentity':adGenEthernetOAMIdentity,'adGenEthernetCfmID':adGenEthernetCfmID,'adGenY1731ID':adGenY1731ID})